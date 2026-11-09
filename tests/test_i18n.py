import csv
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = os.path.join(ROOT, "scripts", "i18n.py")


def run(work, *args):
    p = subprocess.run([sys.executable, TOOL, "--work", work] + list(args),
                       capture_output=True, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return p.returncode, p.stdout.decode("utf-8") + p.stderr.decode("utf-8")


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        if isinstance(data, str):
            f.write(data)
        else:
            json.dump(data, f, ensure_ascii=False)


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def read_csv_rows(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.reader(f))


CSV = (
    "﻿Key,Source,Context,Example,es\r\n"
    "shop.buy,Buy,,,Comprar\r\n"
    "coins.need,\"You need {amount} more coins, hurry!\",,,\r\n"
    "like.reward,Like the game to get a free <b>Lucky Potion</b>!,,,\r\n"
    "multi,\"Line one\nLine two\",,,\r\n"
    ",Settings,,,\r\n"
    "title,Pet Hatch Tycoon,,,\r\n"
)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.work = os.path.join(self.tmp, "work")
        self.csv = os.path.join(self.tmp, "table.csv")
        with open(self.csv, "w", encoding="utf-8", newline="") as f:
            f.write(CSV)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def ingest(self):
        code, out = run(self.work, "ingest", "csv", self.csv)
        self.assertEqual(code, 0, out)

    def loc(self, locale, name):
        return os.path.join(self.work, "locales", locale, name)

    def translate(self, locale, texts, review=None, keep=()):
        todo = read(self.loc(locale, "batch-01.todo.json"))
        draft = {k: {"text": texts[k], "confidence": "high"} for k in todo["keys"]}
        for k in keep:
            draft[k]["keep"] = True
        write(self.loc(locale, "batch-01.draft.json"), draft)
        rev = {k: {"verdict": "ok"} for k in todo["keys"]}
        rev.update(review or {})
        write(self.loc(locale, "batch-01.review.json"), rev)


class LocalesTest(Base):
    def count(self, *args):
        code, out = run(self.work, "locales", *args)
        self.assertEqual(code, 0, out)
        return out.strip().splitlines()[-1]

    def test_modes(self):
        self.assertIn("21 target locales", self.count("main"))
        self.assertIn("49 target locales", self.count("all"))
        self.assertIn("2 target locales", self.count("single", "spanish"))
        self.assertIn("1 target locales", self.count("single", "es-mx"))
        self.assertIn("2 target locales", self.count("single", "Chinese"))
        self.assertIn("1 target locales", self.count("single", "english"))
        self.assertIn("1 target locales", self.count("single", "Português (Brasil)"))

    def test_main_contains_variants(self):
        code, out = run(self.work, "locales", "main")
        for loc in ("en-gb", "fr-ca", "pt-pt", "es-mx", "zh-tw", "ar-001"):
            self.assertIn(loc, out)
        self.assertNotIn("en-us ", out)
        self.assertNotIn("sq-al", out)

    def test_unknown(self):
        code, out = run(self.work, "locales", "single", "klingon")
        self.assertEqual(code, 2)

    def test_loose_names(self):
        for ask in ("norwegian", "simplified chinese", "pt_BR", "Brazilian Portuguese", "tagalog"):
            self.assertIn("1 target locales", self.count("single", ask), ask)


class IngestPlanTest(Base):
    def test_ingest_csv(self):
        self.ingest()
        src = read(os.path.join(self.work, "source.json"))
        keys = [s["key"] for s in src["strings"]]
        self.assertEqual(keys, ["shop.buy", "coins.need", "like.reward", "multi", "Settings", "title"])
        self.assertEqual(src["strings"][3]["source"], "Line one\nLine two")
        self.assertEqual(read(os.path.join(self.work, "existing.json")), {"shop.buy": {"es": "Comprar"}})

    def test_duplicate_key(self):
        with open(self.csv, "a", encoding="utf-8") as f:
            f.write("shop.buy,Buy now,,,\r\n")
        code, out = run(self.work, "ingest", "csv", self.csv)
        self.assertEqual(code, 2)
        self.assertIn("duplicate", out)

    def test_plan_skips_existing_default_variant(self):
        self.ingest()
        code, out = run(self.work, "plan", "single", "spanish")
        self.assertEqual(code, 0, out)
        mx = read(self.loc("es-mx", "batch-01.todo.json"))["keys"]
        es = read(self.loc("es-es", "batch-01.todo.json"))["keys"]
        self.assertNotIn("shop.buy", mx)
        self.assertIn("shop.buy", es)
        self.assertEqual(len(es), 6)

    def test_batches_and_audit(self):
        self.ingest()
        run(self.work, "plan", "single", "es-mx", "--batch", "2")
        self.assertTrue(os.path.exists(self.loc("es-mx", "batch-03.todo.json")))
        self.assertFalse(os.path.exists(self.loc("es-mx", "batch-04.todo.json")))
        code, out = run(self.work, "plan", "single", "es-mx", "--audit")
        self.assertFalse(os.path.exists(self.loc("es-mx", "batch-03.todo.json")))
        audit = read(self.loc("es-mx", "batch-02.todo.json"))
        self.assertEqual(audit["mode"], "audit")
        self.assertEqual(read(self.loc("es-mx", "batch-02.draft.json"))["shop.buy"]["text"], "Comprar")
        # 3 runs for the translate batch, 2 for the audit batch, 1 context analyst.
        self.assertIn("agent runs: about 6", out)
        self.assertIn("context analyst needed: 6 string(s)", out)

    def test_audit_reports_what_a_fix_replaces(self):
        self.ingest()
        run(self.work, "plan", "single", "es-mx", "--audit")
        keys = read(self.loc("es-mx", "batch-01.todo.json"))["keys"]
        write(self.loc("es-mx", "batch-01.draft.json"), {k: {"text": ES[k], "keep": k == "title"} for k in keys})
        write(self.loc("es-mx", "batch-01.review.json"), {k: {"verdict": "ok"} for k in keys})
        write(self.loc("es-mx", "batch-02.review.json"),
              {"shop.buy": {"verdict": "fix", "text": "Compra", "category": "register", "severity": "minor",
                            "reason": "informal imperative"}})
        code, out = run(self.work, "apply", "es-mx")
        self.assertEqual(code, 0, out)
        code, out = run(self.work, "report")
        self.assertIn("## es-mx: changes to existing translations", out)
        self.assertIn("- `shop.buy`: Buy: Comprar -> Compra (informal imperative)", out)


KEYS = ["shop.buy", "coins.need", "like.reward", "multi", "Settings", "title"]


class PackTest(Base):
    def setUp(self):
        super().setUp()
        self.ingest()
        run(self.work, "plan", "single", "es-mx")

    def context(self, **over):
        strings = {k: {"where": "somewhere", "role": "label", "max": None, "params": {}, "neighbors": []}
                   for k in KEYS}
        strings["coins.need"]["params"] = {"amount": {"meaning": "coins missing", "sample": "25"}}
        strings["Settings"]["neighbors"] = ["shop.buy", "title", "gone.key"]
        strings.update(over)
        write(os.path.join(self.work, "context.json"),
              {"game": {"title": "Pet Hatch Tycoon", "tone": "upbeat"}, "strings": strings})

    def test_every_string_needs_context(self):
        code, out = run(self.work, "pack")
        self.assertEqual(code, 2)
        self.assertIn("run the context analyst first", out)
        self.context(multi=None, title={"where": "loading screen"})
        code, out = run(self.work, "pack")
        self.assertEqual(code, 2)
        self.assertIn("1 string(s) have no context entry: multi", out)
        self.assertIn("title: context needs both where and role", out)
        self.assertFalse(os.path.exists(self.loc("es-mx", "batch-01.in.json")))

    def test_bad_max_and_glossary_stop_the_run(self):
        self.context(multi={"where": "x", "role": "label", "max": "40"})
        write(os.path.join(self.work, "glossary.json"),
              {"terms": [{"term": "Rebirth", "decision": "maybe"}, {"term": "Gems", "decision": "translate", "ask": True}]})
        code, out = run(self.work, "pack")
        self.assertEqual(code, 2)
        self.assertIn("multi: max must be a positive number or null", out)
        self.assertIn("glossary term 'Rebirth': decision must be", out)
        self.assertIn("1 glossary term(s) still marked ask", out)

    def test_translator_input(self):
        self.context()
        code, out = run(self.work, "pack")
        self.assertEqual(code, 0, out)
        pack = read(self.loc("es-mx", "batch-01.in.json"))
        self.assertEqual((pack["locale"], pack["mode"], pack["game"]["tone"]), ("es-mx", "translate", "upbeat"))
        self.assertNotIn("shop.buy", pack["strings"])
        need = pack["strings"]["coins.need"]
        self.assertEqual(need["source"], "You need {amount} more coins, hurry!")
        self.assertEqual(need["params"]["amount"]["sample"], "25")
        self.assertNotIn("max", need)
        # A neighbor outside the batch carries the translation players already read.
        self.assertEqual(pack["strings"]["Settings"]["neighbors"],
                         [{"key": "shop.buy", "source": "Buy", "translation": "Comprar"},
                          {"key": "title", "source": "Pet Hatch Tycoon"}])


BIG = [("hud", 40), ("shop", 90), ("pet", 100), ("quest", 70)]


class ContextPartsTest(Base):
    def setUp(self):
        super().setUp()
        self.ingest()

    def part(self, n, kind):
        return os.path.join(self.work, "context", "part-%02d.%s.json" % (n, kind))

    def parts(self):
        folder = os.path.join(self.work, "context")
        return sorted(f for f in os.listdir(folder) if f.endswith(".in.json")) if os.path.isdir(folder) else []

    def big_table(self):
        # Prefixes alternate row by row, so the split has to gather each one.
        rows = sorted(((i, p) for p, n in BIG for i in range(n)), key=lambda r: r[0])
        with open(self.csv, "w", encoding="utf-8", newline="") as f:
            f.write("Key,Source,Context,Example,Location\r\n")
            for i, p in rows:
                f.write("%s.%03d,%s text %d,,shown in %s,\r\n" % (p, i, p, i, p))
            for i in range(20):
                f.write(",Menu text %d,,,StarterGui.Menu.Frame%d.Label\r\n" % (i, i % 3))
        self.ingest()

    def analyst(self, n, terms=(), game=None, **over):
        """Stands in for the analyst of part n."""
        strings = {k: {"where": "screen of part %d" % n, "role": "label", "max": None}
                   for k in read(self.part(n, "in"))["strings"]}
        strings.update(over)
        write(self.part(n, "context"), {"game": game or {"title": "Game %d" % n, "tone": "upbeat"},
                                        "strings": {k: v for k, v in strings.items() if v is not None}})
        write(self.part(n, "glossary"), {"terms": list(terms)})

    def describe_game(self):
        """Stands in for the orchestrator, who writes the game block when the analysts each see a slice."""
        write(os.path.join(self.work, "context.json"), {"game": {"title": "Pet Hatch Tycoon"}, "strings": {}})

    def test_split_keeps_groups_together(self):
        self.big_table()
        code, out = run(self.work, "plan", "single", "es-mx")
        self.assertEqual(code, 0, out)
        # 3 batches of 3 agents, 3 analysts.
        self.assertIn("agent runs: about 12", out)
        self.assertIn("context analyst needed: 320 string(s) have no context entry yet, in 3 part(s)", out)
        self.assertIn("no analyst will see the whole table: write the game block", out)
        parts = [read(self.part(n, "in")) for n in (1, 2, 3)]
        keys = [k for p in parts for k in p["strings"]]
        self.assertEqual((len(keys), len(set(keys))), (320, 320))
        self.assertLessEqual(max(len(p["strings"]) for p in parts), 150)
        for prefix, count in BIG + [("Menu text", 20)]:
            homes = [sum(k.startswith(prefix) for k in p["strings"]) for p in parts]
            self.assertEqual(sorted(homes), [0, 0, count], prefix)
        self.assertEqual((parts[0]["part"], parts[0]["parts"]), (1, 3))
        self.assertEqual(parts[0]["strings"]["hud.000"], {"source": "hud text 0", "example": "shown in hud"})
        self.assertIn("location", parts[1]["strings"]["Menu text 0"])
        self.assertNotIn("game", parts[0])
        code, out = run(self.work, "status")
        self.assertIn("context p1:in p2:in p3:in", out)

    def test_resplit_smaller_and_plan_keeps_it(self):
        self.big_table()
        run(self.work, "plan", "single", "es-mx")
        code, out = run(self.work, "contextpack", "--part", "100")
        self.assertEqual(code, 0, out)
        self.assertIn("contextpack: 4 part(s), 320 string(s)", out)
        self.assertLessEqual(max(len(read(self.part(n, "in"))["strings"]) for n in (1, 2, 3, 4)), 100)
        self.assertTrue(os.path.exists(os.path.join(self.work, "context", "history", "001", "part-03.in.json")))
        code, out = run(self.work, "plan", "single", "es-mx")
        self.assertIn("in 4 part(s)", out)
        self.assertEqual(len(self.parts()), 4)

    def test_split_cuts_only_a_group_too_big_for_one_part(self):
        strings = [{"key": "item.%03d" % i, "source": "x", "keyless": False} for i in range(400)]
        self.assertEqual([len(p) for p in i18n.split_context(strings, 150)], [134, 134, 132])
        strings = [{"key": "%s.%d" % (p, i), "source": "x", "keyless": False}
                   for p, n in (("a", 149), ("b", 2), ("c", 149)) for i in range(n)]
        self.assertEqual([len(p) for p in i18n.split_context(strings, 150)], [149, 2, 149])
        self.assertEqual(i18n.split_context([], 150), [])

    def test_small_table_is_one_part(self):
        code, out = run(self.work, "plan", "single", "es-es")
        self.assertIn("context analyst needed: 6 string(s) have no context entry yet, in 1 part(s)", out)
        self.assertNotIn("no analyst will see the whole table", out)
        self.assertEqual(self.parts(), ["part-01.in.json"])
        self.analyst(1, terms=[{"term": "Pet Hatch Tycoon", "decision": "keep"}])
        code, out = run(self.work, "pack")
        self.assertEqual(code, 0, out)
        self.assertEqual(read(os.path.join(self.work, "context.json"))["game"]["title"], "Game 1")
        self.assertEqual(read(self.loc("es-es", "batch-01.in.json"))["strings"]["title"]["where"], "screen of part 1")

    def test_merge_keeps_earlier_entries(self):
        earlier = {"where": "under each shop item", "role": "button", "max": 8}
        write(os.path.join(self.work, "context.json"),
              {"game": {"title": "Pet Hatch Tycoon", "tone": "cozy"}, "strings": {"shop.buy": earlier}})
        write(os.path.join(self.work, "glossary.json"),
              {"terms": [{"term": "Pet Hatch Tycoon", "decision": "keep"}, {"term": "Coins", "decision": "translate"}]})
        run(self.work, "plan", "single", "es-es")
        code, out = run(self.work, "contextpack", "--part", "3")
        self.assertIn("contextpack: 2 part(s), 5 string(s)", out)
        first = read(self.part(1, "in"))
        self.assertEqual(first["game"]["tone"], "cozy")
        self.assertNotIn("shop.buy", list(first["strings"]) + list(read(self.part(2, "in"))["strings"]))
        potion = {"term": "Lucky Potion", "meaning": "boost item", "decision": "translate", "reason": "ordinary words"}
        self.analyst(1, terms=[potion, {"term": "Coins", "decision": "keep"}],
                     **{"shop.buy": {"where": "somewhere else", "role": "label"}})
        self.analyst(2, terms=[dict(potion, meaning="a potion"), {"term": "Robux", "decision": "keep", "ask": True}])
        code, out = run(self.work, "pack")
        self.assertEqual(code, 0, out)
        self.assertIn("context: merged 2 part(s): 5 string(s), 2 new glossary term(s)", out)
        self.assertNotIn("conflict", out)
        ctx = read(os.path.join(self.work, "context.json"))
        self.assertEqual(ctx["game"], {"title": "Pet Hatch Tycoon", "tone": "cozy"})
        self.assertEqual(sorted(ctx["strings"]), sorted(KEYS))
        self.assertEqual(ctx["strings"]["shop.buy"], earlier)
        terms = read(os.path.join(self.work, "glossary.json"))["terms"]
        self.assertEqual([(t["term"], t["decision"]) for t in terms],
                         [("Pet Hatch Tycoon", "keep"), ("Coins", "translate"), ("Lucky Potion", "translate"),
                          ("Robux", "keep")])
        self.assertEqual(terms[2]["meaning"], "boost item")
        self.assertTrue(terms[3]["ask"])
        # Merged parts leave the folder, so a later pack cannot undo an edit made at the checkpoint.
        self.assertEqual(self.parts(), [])
        self.assertTrue(os.path.exists(os.path.join(self.work, "context", "history", "002", "part-02.glossary.json")))
        terms[2]["decision"] = "keep"
        write(os.path.join(self.work, "glossary.json"), {"terms": terms})
        code, out = run(self.work, "pack")
        self.assertEqual(code, 0, out)
        self.assertEqual(read(os.path.join(self.work, "glossary.json"))["terms"][2]["decision"], "keep")
        self.assertEqual(read(os.path.join(self.work, "context.json")), ctx)
        # A later run asks only for what is new, and hands the analyst the game block.
        with open(self.csv, "a", encoding="utf-8") as f:
            f.write("shop.sell,Sell,,,\r\n")
        self.ingest()
        code, out = run(self.work, "plan", "single", "es-es")
        self.assertIn("context analyst needed: 1 string(s) have no context entry yet, in 1 part(s)", out)
        later = read(self.part(1, "in"))
        self.assertEqual((list(later["strings"]), later["game"]["tone"]), (["shop.sell"], "cozy"))

    def test_sliced_table_needs_a_game_block_from_the_orchestrator(self):
        run(self.work, "plan", "single", "es-es")
        code, out = run(self.work, "contextpack", "--part", "3")
        self.assertIn("no analyst will see the whole table: write the game block", out)
        self.analyst(1)
        self.analyst(2)
        code, out = run(self.work, "pack")
        self.assertEqual(code, 2, out)
        self.assertIn("context.json has no game block, and no analyst saw the whole table", out)
        self.assertEqual(len(self.parts()), 2)
        self.describe_game()
        # Splitting again only hands the block to each part; the analysts' files stay.
        code, out = run(self.work, "contextpack")
        self.assertNotIn("no analyst will see the whole table", out)
        self.assertEqual(read(self.part(2, "in"))["game"], {"title": "Pet Hatch Tycoon"})
        self.assertTrue(os.path.exists(self.part(2, "context")))
        code, out = run(self.work, "pack")
        self.assertEqual(code, 0, out)
        ctx = read(os.path.join(self.work, "context.json"))
        self.assertEqual(ctx["game"], {"title": "Pet Hatch Tycoon"})
        self.assertEqual(sorted(ctx["strings"]), sorted(KEYS))

    def test_glossary_conflict_goes_to_the_user(self):
        self.describe_game()
        run(self.work, "plan", "single", "es-es")
        run(self.work, "contextpack", "--part", "3")
        # HATCH (a promo code) and Hatch (the verb) are two terms, not one term decided twice.
        self.analyst(1, terms=[{"term": "Lucky Potion", "decision": "translate", "reason": "ordinary words"},
                               {"term": "HATCH", "decision": "keep", "reason": "promo code"}])
        self.analyst(2, terms=[{"term": "Lucky Potion", "decision": "keep", "reason": "product name"},
                               {"term": "Hatch", "decision": "translate"}])
        code, out = run(self.work, "pack")
        self.assertEqual(code, 2, out)
        self.assertIn("conflict Lucky Potion: part 1: translate (ordinary words); part 2: keep (product name)", out)
        self.assertIn("ERROR glossary term 'Lucky Potion': analysts disagreed", out)
        self.assertFalse(os.path.exists(self.loc("es-es", "batch-01.in.json")))
        self.assertEqual(read(os.path.join(self.work, "context.json"))["game"], {"title": "Pet Hatch Tycoon"})
        path = os.path.join(self.work, "glossary.json")
        terms = read(path)["terms"]
        self.assertEqual([(t["term"], t["decision"], t.get("ask")) for t in terms],
                         [("Lucky Potion", "translate", True), ("HATCH", "keep", None), ("Hatch", "translate", None)])
        self.assertIn("part 2: keep (product name)", terms[0]["conflict"])
        self.assertNotIn("conflict", terms[1])
        # The conflict stays an error on every pack until someone settles it.
        self.assertEqual(run(self.work, "pack")[0], 2)
        del terms[0]["conflict"]
        terms[0]["ask"] = False
        write(path, {"terms": terms})
        code, out = run(self.work, "pack")
        self.assertEqual(code, 0, out)
        self.assertTrue(os.path.exists(self.loc("es-es", "batch-01.in.json")))

    def test_unfinished_part_merges_nothing(self):
        self.describe_game()
        run(self.work, "plan", "single", "es-es")
        run(self.work, "contextpack", "--part", "3")
        self.analyst(1)
        code, out = run(self.work, "pack")
        self.assertEqual(code, 2, out)
        self.assertIn("ERROR part 2: no", out)
        self.assertIn("run the context analyst first", out)
        second = list(read(self.part(2, "in"))["strings"])
        self.analyst(2, terms=[{"term": "Gems", "decision": "maybe"}],
                     **{second[0]: None, second[1]: {"where": "shop"}})
        code, out = run(self.work, "pack")
        self.assertEqual(code, 2, out)
        self.assertIn("part-02.context.json: 1 string(s) have no context entry: " + second[0], out)
        self.assertIn("part-02.context.json: %s: context needs both where and role" % second[1], out)
        self.assertIn("part-02.glossary.json: glossary term 'Gems': decision must be", out)
        self.assertEqual(read(os.path.join(self.work, "context.json"))["strings"], {})
        self.assertFalse(os.path.exists(os.path.join(self.work, "glossary.json")))
        self.assertEqual(len(self.parts()), 2)
        self.analyst(2)
        code, out = run(self.work, "pack")
        self.assertEqual(code, 0, out)
        self.assertEqual(sorted(read(os.path.join(self.work, "context.json"))["strings"]), sorted(KEYS))


KEYLESS_CSV = (
    "Key,Source,Context,Example,Location\r\n"
    ",Play,,,StarterGui.Menu.PlayButton\r\n"
    ",Play,Workspace.Stage.Sign,,\r\n"
    "Open,Open,,,\r\n"
    "buy,Buy for {price:int} Robux,,,\r\n"
    "need,Need {amount} coins,,,\r\n"
)
DE = {"Play": "Spielen", "Play | Workspace.Stage.Sign": "Theaterstück", "Open": "Öffnen",
      "buy": "Für {price:int} Robux kaufen", "need": "Dir fehlen {amount} Münzen"}


class KeylessTest(Base):
    def setUp(self):
        super().setUp()
        with open(self.csv, "w", encoding="utf-8", newline="") as f:
            f.write(KEYLESS_CSV)
        self.ingest()

    def finish(self):
        write(os.path.join(self.work, "context.json"),
              {"strings": {"buy": {"params": {"price": {"sample": "1,250"}}},
                           "need": {"params": {"amount": {"sample": 25}}}}})
        run(self.work, "plan", "single", "de-de")
        self.translate("de-de", DE)
        code, out = run(self.work, "apply", "de-de")
        self.assertIn("clean", out)

    def test_source_plus_context_is_the_identity(self):
        strings = read(os.path.join(self.work, "source.json"))["strings"]
        self.assertEqual([s["key"] for s in strings], list(DE))
        self.assertEqual([s.get("keyless", False) for s in strings], [True, True, False, False, False])
        self.assertEqual(strings[0]["location"], "StarterGui.Menu.PlayButton")
        with open(self.csv, "a", encoding="utf-8", newline="") as f:
            f.write(",Play,Workspace.Stage.Sign,,\r\n")
        code, out = run(self.work, "ingest", "csv", self.csv)
        self.assertEqual(code, 2)
        self.assertIn("duplicate", out)

    def test_csv_rows_match_by_context(self):
        self.finish()
        outp = os.path.join(self.tmp, "de.csv")
        code, out = run(self.work, "export", "csv", "--out", outp)
        self.assertEqual(code, 0, out)
        rows = read_csv_rows(outp)
        col = rows[0].index("de-de")
        self.assertEqual(rows[0][4], "Location")
        self.assertEqual([r[col] for r in rows[1:4]], ["Spielen", "Theaterstück", "Öffnen"])
        self.assertEqual(rows[1][4], "StarterGui.Menu.PlayButton")
        code, out = run(self.work, "check", outp)
        self.assertEqual(code, 0, out)

    def luau_json(self, name):
        with open(os.path.join(self.work, "out", "studio", name), encoding="utf-8") as f:
            text = f.read()
        return text, json.loads(text[text.index("[=[") + 3:text.index("]=]")])

    def test_studio_keeps_a_key_equal_to_its_source(self):
        self.finish()
        code, out = run(self.work, "export", "studio")
        self.assertEqual(code, 0, out)
        text, data = self.luau_json("load-01.luau")
        self.assertEqual([(d["key"], d["context"]) for d in data[:3]],
                         [("", ""), ("", "Workspace.Stage.Sign"), ("Open", "")])
        self.assertIn("FinishRecordingOperation.Cancel", text)

    def test_verify_samples(self):
        self.finish()
        run(self.work, "export", "studio")
        code, out = run(self.work, "studio", "verify")
        self.assertEqual(code, 0, out)
        cases = {c["key"]: c for c in self.luau_json("verify-01.luau")[1]["de-de"]}
        self.assertEqual(sorted(cases), ["Open", "buy", "need"])
        # A Lua number in a plain {param} would render as 25.00.
        self.assertEqual(cases["need"], {"key": "need", "args": {"amount": "25"}, "expect": "Dir fehlen 25 Münzen"})
        self.assertEqual(cases["buy"], {"key": "buy", "args": {"price": 1250}})


ES = {
    "shop.buy": "Comprar",
    "coins.need": "¡Te faltan {amount} monedas, apúrate!",
    "like.reward": "¡Dale like al juego y llévate una <b>Poción de la Suerte</b> gratis!",
    "multi": "Línea uno\nLínea dos",
    "Settings": "Configuración",
    "title": "Pet Hatch Tycoon",
}


sys.path.insert(0, os.path.join(ROOT, "scripts"))
import i18n  # noqa: E402


class KeepTermTest(unittest.TestCase):
    def test_whole_word(self):
        es = {"id": "es-es", "code": "es", "script": "Latn"}
        e, _ = i18n.lint_string("k", "Enter a code", "Introduce un código", es, {}, {}, ["E"], False)
        self.assertEqual(e, [])
        e, _ = i18n.lint_string("k", "Press E to sell", "Pulsa para vender", es, {}, {}, ["E"], False)
        self.assertIn("keep-term 'E' missing", e)
        et = {"id": "et-ee", "code": "et", "script": "Latn"}
        e, _ = i18n.lint_string("k", "Buy for {price} Robux", "Osta {price} Robuxi eest", et, {}, {}, ["Robux"], False)
        self.assertEqual(e, [])
        ja = {"id": "ja-jp", "code": "ja", "script": "Jpan"}
        e, _ = i18n.lint_string("k", "Buy for {price} Robux", "{price} Robuxで購入", ja, {}, {}, ["Robux"], False)
        self.assertEqual(e, [])

    def test_locale_latin_terms_and_georgian(self):
        my = {"id": "my-mm", "code": "my", "script": "Mymr"}
        src, txt = "Rebirth Boost Event", "Rebirth Boost Event ရပ်"
        e, _ = i18n.lint_string("k", src, txt, my, {}, {}, [], False)
        self.assertTrue(any("mostly not in Mymr" in m for m in e))
        e, _ = i18n.lint_string("k", src, txt, my, {}, {}, [], False, ["Rebirth", "Boost", "Event"])
        self.assertEqual(e, [])
        ka = {"id": "ka-ge", "code": "ka", "script": "Geor"}
        e, _ = i18n.lint_string("k", "Shop", "ᲘᲐᲦᲐᲨᲘ", ka, {}, {}, [], False)
        self.assertTrue(any("Mtavruli" in m for m in e))

    def test_chinese_sets_disjoint(self):
        self.assertEqual(i18n.SIMPLIFIED_ONLY & i18n.TRADITIONAL_ONLY, set())

    def test_width_counts_spacing_marks(self):
        self.assertEqual(i18n.width("खरीदें"), 4)
        self.assertEqual(i18n.width("{n} <b>購入</b>"), 5)

    def lint(self, source, text, locale="es-es", script="Latn", item=None, keep=()):
        loc = {"id": locale, "code": locale.split("-")[0], "script": script}
        return i18n.lint_string("k", source, text, loc, item or {}, {}, list(keep), False)

    def test_nothing_to_translate(self):
        self.assertEqual(self.lint("{count}", "{count}")[0], [])
        self.assertEqual(self.lint("100%", "100%")[0], [])
        self.assertEqual(self.lint("{price} Robux", "{price} Robux", keep=["Robux"])[0], [])
        self.assertIn("identical to source without keep:true", self.lint("Shop", "Shop")[0])

    def test_ordinal_marks_are_latin(self):
        self.assertEqual(self.lint("1st place", "1.º lugar", "pt-br"), ([], []))
        self.assertTrue(any("non-Latin" in m for m in self.lint("Buy", "Купить", "pt-br")[0]))

    def test_tag_attributes_must_survive(self):
        src = '<font color="#FF0000">Sale</font> today'
        self.assertEqual(self.lint(src, "Hoy: <font color='#ff0000'>Oferta</font>")[0], [])
        e, _ = self.lint(src, '<font color="rojo">Oferta</font> hoy')
        self.assertTrue(any("rich-text tags differ" in m for m in e))

    def test_number_mismatch_warns(self):
        _, w = self.lint("50% off", "5% de descuento")
        self.assertTrue(any("numbers differ" in m for m in w))
        self.assertEqual(self.lint("50% off", "Mitad de precio", item={"note": "idiom"})[1], [])
        self.assertEqual(self.lint("Level 50", "المستوى ٥٠", "ar-001", "Arab")[1], [])
        self.assertEqual(self.lint("1,000 coins", "1.000 monedas")[1], [])

    def test_latin_acronym_needs_keep(self):
        e, _ = self.lint("Music", "BGM", "ja-jp", "Jpan")
        self.assertTrue(any("set keep:true" in m for m in e))
        self.assertEqual(self.lint("Music", "BGM", "ja-jp", "Jpan", item={"keep": True, "note": "usual label"})[0], [])


class ApplyLintTest(Base):
    def setUp(self):
        super().setUp()
        self.ingest()
        write(os.path.join(self.work, "glossary.json"),
              {"terms": [{"term": "Pet Hatch Tycoon", "decision": "keep"}]})

    def test_clean_apply(self):
        run(self.work, "plan", "single", "es-es")
        self.translate("es-es", ES, keep=("title",))
        code, out = run(self.work, "apply", "es-es")
        self.assertIn("clean", out)
        code, out = run(self.work, "lint")
        self.assertEqual(code, 0, out)

    def test_lint_errors(self):
        run(self.work, "plan", "single", "es-es")
        bad = dict(ES)
        bad["coins.need"] = "Te faltan {cantidad} monedas"
        bad["like.reward"] = "Dale like y llévate una Poción gratis"
        bad["Settings"] = "Settings"
        bad["title"] = "Juego de Mascotas"
        self.translate("es-es", bad)
        code, out = run(self.work, "apply", "es-es")
        self.assertIn("params differ", out)
        self.assertIn("rich-text tags differ", out)
        self.assertIn("identical to source without keep", out)
        self.assertIn("keep-term 'Pet Hatch Tycoon' missing", out)
        self.assertIn("resolve round needed", out)
        code, _ = run(self.work, "lint")
        self.assertEqual(code, 1)

    def test_review_resolve_decide(self):
        run(self.work, "plan", "single", "es-es")
        self.translate("es-es", ES, keep=("title",), review={
            "shop.buy": {"verdict": "fix", "text": "Comprar ya", "category": "fluency", "severity": "minor", "reason": "x"},
            "Settings": {"verdict": "fix", "text": "Ajustes", "category": "locale", "severity": "major", "reason": "Spain"}})
        code, out = run(self.work, "apply", "es-es")
        self.assertIn("resolve round needed for 1 key(s): Settings", out)
        fin = read(self.loc("es-es", "final.json"))
        self.assertEqual(fin["shop.buy"]["text"], "Comprar ya")
        self.assertEqual(fin["shop.buy"]["status"], "fixed")
        write(self.loc("es-es", "batch-01.resolve.json"),
              {"Settings": {"accept": False, "text": "Configuración", "reason": "both used"}})
        code, out = run(self.work, "apply", "es-es", "--resolve")
        self.assertIn("1 dispute(s)", out)
        self.assertEqual(read(self.loc("es-es", "final.json"))["Settings"]["status"], "disputed")
        write(self.loc("es-es", "decisions.json"), {"Settings": {"text": "Ajustes", "reason": "Spain UI uses Ajustes"}})
        code, out = run(self.work, "apply", "es-es", "--resolve")
        fin = read(self.loc("es-es", "final.json"))
        self.assertEqual(fin["Settings"]["text"], "Ajustes")
        self.assertEqual(fin["Settings"]["status"], "decided")
        self.assertFalse(os.path.exists(self.loc("es-es", "disputes.json")))

    def test_broken_agent_files_name_the_file(self):
        run(self.work, "plan", "single", "es-es")
        self.translate("es-es", ES, keep=("title",))
        review = self.loc("es-es", "batch-01.review.json")
        good = read(review)
        write(review, '{"shop.buy": {"verdict": "ok"},')
        code, out = run(self.work, "apply", "es-es")
        self.assertEqual(code, 2)
        self.assertIn("invalid JSON", out)
        self.assertIn("batch-01.review.json", out)
        write(review, dict(good, title={"verdict": "fix", "text": "Pet Hatch Tycoon", "severity": "high"}))
        code, out = run(self.work, "apply", "es-es")
        self.assertEqual(code, 2)
        self.assertIn("title (severity must be minor, major or critical)", out)
        write(review, good)
        write(self.loc("es-es", "batch-01.draft.json"), dict(read(self.loc("es-es", "batch-01.draft.json")), multi="x"))
        code, out = run(self.work, "apply", "es-es")
        self.assertEqual(code, 2)
        self.assertIn('1 key(s) missing or without "text": multi', out)
        self.assertFalse(os.path.exists(self.loc("es-es", "final.json")))

    def test_wrapped_agent_files_are_flattened(self):
        run(self.work, "plan", "single", "es-es")
        self.translate("es-es", ES, keep=("title",))
        for name, wrapper in (("batch-01.draft.json", "strings"), ("batch-01.review.json", "strings")):
            write(self.loc("es-es", name), {"locale": "es-es", wrapper: read(self.loc("es-es", name))})
        write(self.loc("es-es", "terms.json"), {"locale": "es-es", "terms": {"Coins": "Monedas"}})
        code, out = run(self.work, "apply", "es-es")
        self.assertEqual(code, 0, out)
        self.assertIn("clean", out)
        self.assertEqual(read(self.loc("es-es", "terms.json")), {"Coins": "Monedas"})
        self.assertEqual(read(self.loc("es-es", "batch-01.review.json"))["shop.buy"], {"verdict": "ok"})
        write(self.loc("es-es", "terms.json"), {"Coins": {"text": "Monedas"}})
        code, out = run(self.work, "backpack", "es-es", "1")
        self.assertEqual(code, 2)
        self.assertIn("terms.json must be one flat object", out)

    def test_held_back_string_is_not_shipped(self):
        run(self.work, "plan", "single", "es-es")
        self.translate("es-es", dict(ES, Settings="Settings"), keep=("title",))
        code, out = run(self.work, "apply", "es-es")
        self.assertIn("identical to source", out)
        write(self.loc("es-es", "decisions.json"), {"Settings": {"needs_native": True, "reason": "no safe wording"}})
        code, out = run(self.work, "apply", "es-es")
        self.assertIn("clean", out)
        self.assertEqual(run(self.work, "lint")[0], 0)
        outp = os.path.join(self.tmp, "held.csv")
        run(self.work, "export", "csv", "--out", outp)
        rows = read_csv_rows(outp)
        self.assertIn("es-es", rows[0])
        self.assertNotIn("Settings", [r[0] or r[1] for r in rows[1:]])
        self.assertEqual(run(self.work, "check", outp)[0], 0)

    def lint_one(self, locale, text, source_key="shop.buy"):
        run(self.work, "plan", "single", locale)
        todo = read(self.loc(locale, "batch-01.todo.json"))["keys"]
        texts = {k: ES[k] for k in todo}
        texts[source_key] = text
        keep = [k for k in todo if k != source_key]
        self.translate(locale, texts, keep=keep)
        code, out = run(self.work, "apply", locale)
        return out

    def test_script_checks(self):
        self.assertIn("mostly not in Jpan", self.lint_one("ja-jp", "Comprar ahora"))
        self.assertIn("Simplified-only", self.lint_one("zh-tw", "购买"))
        self.assertIn("Traditional-only", self.lint_one("zh-cn", "購買"))
        self.assertIn("cedilla", self.lint_one("ro-ro", "Cumpăraţi"))
        self.assertIn("non-Latin letters", self.lint_one("de-de", "Kaufen 买"))
        self.assertIn("Zawgyi", self.lint_one("my-mm", "ေကာင္း"))

    def test_script_passes(self):
        self.assertIn("clean", self.lint_one("ja-jp", "購入"))
        self.assertIn("clean", self.lint_one("zh-tw", "購買"))
        self.assertIn("clean", self.lint_one("uk-ua", "Купити"))
        self.assertIn("clean", self.lint_one("my-mm", "ဝယ်မည်"))

    def test_length_budget(self):
        write(os.path.join(self.work, "context.json"), {"strings": {"shop.buy": {"max": 6, "role": "button"}}})
        self.assertIn("over twice the budget", self.lint_one("es-es", "Comprar este objeto ahora"))
        self.assertIn("over budget 6 with no note", self.lint_one("it-it", "Comprarlo"))


class ExportTest(Base):
    def setUp(self):
        super().setUp()
        self.ingest()
        write(os.path.join(self.work, "glossary.json"), {"terms": [{"term": "Pet Hatch Tycoon", "decision": "keep"}]})

    def finish(self, locale, texts):
        self.translate(locale, {k: texts[k] for k in read(self.loc(locale, "batch-01.todo.json"))["keys"]},
                       keep=("title",))
        code, out = run(self.work, "apply", locale)
        self.assertIn("clean", out)

    def test_csv_columns_and_roundtrip(self):
        run(self.work, "plan", "single", "spanish")
        es_es = dict(ES, Settings="Ajustes")
        self.finish("es-es", es_es)
        self.finish("es-mx", ES)
        outp = os.path.join(self.tmp, "out", "upload.csv")
        code, out = run(self.work, "export", "csv", "--out", outp)
        self.assertEqual(code, 0, out)
        rows = read_csv_rows(outp)
        header = rows[0]
        self.assertEqual(header[:5], ["Key", "Source", "Context", "Example", "es"])
        self.assertIn("es-es", header)
        self.assertIn("es-mx", header)
        by = {r[0] or r[1]: dict(zip(header, r)) for r in rows[1:]}
        self.assertEqual(by["Settings"]["es-es"], "Ajustes")
        self.assertEqual(by["Settings"]["es-mx"], "Configuración")
        self.assertEqual(by["Settings"]["es"], "Configuración")
        self.assertEqual(by["shop.buy"]["es"], "Comprar")
        self.assertEqual(by["multi"]["Source"], "Line one\nLine two")
        state = read(os.path.join(self.work, "state.json"))
        self.assertIn("es-mx", state["Settings"])
        code, out = run(self.work, "plan", "single", "spanish")
        self.assertIn("0 need work", out)
        self.assertFalse(os.path.exists(self.loc("es-mx", "batch-01.draft.json")))
        self.assertTrue(os.path.exists(self.loc("es-mx", os.path.join("history", "001", "batch-01.draft.json"))))
        code, out = run(self.work, "apply", "es-mx")
        self.assertEqual(code, 2)

    def test_status_before_plan(self):
        code, out = run(self.work, "status")
        self.assertEqual(code, 0, out)
        self.assertIn("6 strings", out)

    def test_backpack_is_blind(self):
        write(os.path.join(self.work, "context.json"),
              {"strings": {"title": {"role": "title", "where": "loading screen, shows Pet Hatch Tycoon"},
                           "shop.buy": {"role": "button", "where": "the Buy button for buyers, next to coins.need"}}})
        run(self.work, "plan", "single", "es-es")
        self.translate("es-es", ES, keep=("title",))
        code, out = run(self.work, "backpack", "es-es", "1")
        self.assertEqual(code, 0, out)
        pack = read(self.loc("es-es", "batch-01.backin.json"))
        self.assertEqual(sorted(pack), ["s001", "s002", "s003", "s004", "s005", "s006"])
        self.assertEqual(pack["s001"]["text"], "Comprar")
        self.assertEqual(pack["s001"]["where"], "the [name] button for buyers, next to [name]")
        self.assertNotIn("Pet Hatch Tycoon", pack["s006"]["where"])

    def test_reviewpack_joins_the_blind_back_translation(self):
        write(os.path.join(self.work, "context.json"),
              {"strings": {"shop.buy": {"role": "button", "where": "under each item", "max": 8}}})
        run(self.work, "plan", "single", "es-es")
        self.translate("es-es", dict(ES, **{"coins.need": "Te faltan monedas"}), keep=("title",))
        code, out = run(self.work, "reviewpack", "es-es", "1")
        self.assertEqual(code, 2, out)
        run(self.work, "backpack", "es-es", "1")
        back = {i: "meaning of " + i for i in read(self.loc("es-es", "batch-01.backin.json"))}
        back["s001"] = "Buy [formal for a button]"
        del back["s003"]
        write(self.loc("es-es", "batch-01.back.json"), back)
        code, out = run(self.work, "reviewpack", "es-es", "1")
        self.assertEqual(code, 2)
        self.assertIn("no back-translation for 1 string(s): s003", out)
        back["s003"] = "Like the game for a free Lucky Potion"
        write(self.loc("es-es", "batch-01.back.json"), back)
        code, out = run(self.work, "reviewpack", "es-es", "1")
        self.assertEqual(code, 0, out)
        strings = read(self.loc("es-es", "batch-01.reviewin.json"))["strings"]
        self.assertEqual(strings["shop.buy"]["source"], "Buy")
        self.assertEqual(strings["shop.buy"]["text"], "Comprar")
        self.assertEqual(strings["shop.buy"]["back"], "Buy [formal for a button]")
        self.assertEqual(strings["shop.buy"]["max"], 8)
        self.assertTrue(any("params differ" in m for m in strings["coins.need"]["lint"]))
        run(self.work, "apply", "es-es")
        self.assertEqual(read(self.loc("es-es", "final.json"))["shop.buy"]["blind_remark"], "formal for a button")

    def test_deleted_string_is_pruned(self):
        run(self.work, "plan", "single", "es-mx")
        self.finish("es-mx", ES)
        with open(self.csv, "w", encoding="utf-8", newline="") as f:
            f.write("".join(line for line in CSV.splitlines(True) if not line.startswith("title,")))
        self.ingest()
        code, out = run(self.work, "plan", "single", "es-mx")
        self.assertIn("0 need work", out)
        self.assertNotIn("title", read(self.loc("es-mx", "final.json")))
        code, out = run(self.work, "lint", "es-mx")
        self.assertEqual(code, 0, out)

    def test_language_columns_keep_a_fixed_order(self):
        run(self.work, "plan", "main")
        for locale in ("it-it", "id-id", "de-de"):
            self.finish(locale, ES)
        headers = set()
        for seed in ("0", "1", "2", "3"):
            outp = os.path.join(self.tmp, "lang%s.csv" % seed)
            p = subprocess.run([sys.executable, TOOL, "--work", self.work, "export", "csv", "--out", outp,
                                "--columns", "language"], capture_output=True,
                               env=dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONHASHSEED=seed))
            self.assertEqual(p.returncode, 0, p.stderr)
            headers.add(tuple(read_csv_rows(outp)[0]))
        self.assertEqual(headers, {("Key", "Source", "Context", "Example", "es", "de", "id", "it")})

    def test_split_by_file_size(self):
        big = os.path.join(self.tmp, "big.csv")
        with open(big, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Key", "Source", "Context", "Example"])
            for i in range(300):
                w.writerow(["k%d" % i, "Item %d" % i, "", ""])
        run(self.work, "ingest", "csv", big)
        run(self.work, "plan", "single", "de-de", "--batch", "2000")
        keys = read(self.loc("de-de", "batch-01.todo.json"))["keys"]
        write(self.loc("de-de", "batch-01.draft.json"), {k: {"text": k[1:] + " " + "lang " * 1600} for k in keys})
        write(self.loc("de-de", "batch-01.review.json"), {k: {"verdict": "ok"} for k in keys})
        run(self.work, "apply", "de-de")
        outp = os.path.join(self.tmp, "out", "de.csv")
        code, out = run(self.work, "export", "csv", "--out", outp)
        self.assertEqual(code, 0, out)
        parts = sorted(x for x in os.listdir(os.path.dirname(outp)) if x.startswith("de-part"))
        self.assertEqual(len(parts), 2, out)
        rows = 0
        for name in parts:
            path = os.path.join(os.path.dirname(outp), name)
            self.assertLess(os.path.getsize(path), 2 * 1024 * 1024)
            rows += len(read_csv_rows(path)) - 1
        self.assertEqual(rows, 300)
        self.assertNotIn("over Roblox", out)

    def test_check_exported_csv(self):
        run(self.work, "plan", "single", "es-mx")
        self.finish("es-mx", ES)
        outp = os.path.join(self.tmp, "check.csv")
        run(self.work, "export", "csv", "--out", outp)
        code, out = run(self.work, "check", outp)
        self.assertEqual(code, 0, out)
        rows = read_csv_rows(outp)
        col = rows[0].index("es-mx")
        for r in rows[1:]:
            if r[0] == "coins.need":
                r[col] = "Te faltan monedas"
        with open(outp, "w", encoding="utf-8", newline="") as fh:
            csv.writer(fh).writerows(rows)
        code, out = run(self.work, "check", outp)
        self.assertEqual(code, 1)
        self.assertIn("params differ", out)
        self.assertIn("differs from final.json", out)

    def test_english_variant_writes_source_columns(self):
        run(self.work, "plan", "single", "en-gb")
        self.finish("en-gb", {"shop.buy": "Buy", "coins.need": "You need {amount} more coins, hurry!",
                              "like.reward": "Like the game to get a free <b>Lucky Potion</b>!",
                              "multi": "Line one\nLine two", "Settings": "Settings", "title": "Pet Hatch Tycoon"})
        outp = os.path.join(self.tmp, "en.csv")
        run(self.work, "export", "csv", "--out", outp)
        header = read_csv_rows(outp)[0]
        for col in ("en", "en-us", "en-gb"):
            self.assertIn(col, header)

    def test_rojo_in_place_and_language_columns(self):
        run(self.work, "plan", "single", "es-es")
        self.finish("es-es", dict(ES, Settings="Ajustes"))
        code, out = run(self.work, "export", "csv", "--rojo", self.csv, "--columns", "language")
        self.assertEqual(code, 0, out)
        with open(self.csv, "rb") as f:
            raw = f.read()
        self.assertTrue(raw.startswith(b"\xef\xbb\xbf"))
        rows = read_csv_rows(self.csv)
        self.assertEqual(rows[0], ["Key", "Source", "Context", "Example", "es"])
        self.assertEqual(len(rows), 7)
        by = {r[0] or r[1]: r for r in rows[1:]}
        self.assertEqual(by["Settings"][4], "Ajustes")

    def test_split_at_1000(self):
        big = os.path.join(self.tmp, "big.csv")
        with open(big, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Key", "Source", "Context", "Example"])
            for i in range(1201):
                w.writerow(["k%d" % i, "Item %d" % i, "", ""])
        run(self.work, "ingest", "csv", big)
        run(self.work, "plan", "single", "de-de", "--batch", "2000")
        keys = read(self.loc("de-de", "batch-01.todo.json"))["keys"]
        write(self.loc("de-de", "batch-01.draft.json"), {k: {"text": "Gegenstand " + k[1:]} for k in keys})
        write(self.loc("de-de", "batch-01.review.json"), {k: {"verdict": "ok"} for k in keys})
        run(self.work, "apply", "de-de")
        outp = os.path.join(self.tmp, "out", "de.csv")
        code, out = run(self.work, "export", "csv", "--out", outp)
        self.assertIn("de-part1.csv: 1000 changed rows", out)
        self.assertIn("de-part2.csv: 201 changed rows", out)

    def test_studio_chunks(self):
        run(self.work, "plan", "single", "es-mx")
        self.finish("es-mx", dict(ES, title="Pet Hatch Tycoon ]=]"))
        code, out = run(self.work, "export", "studio", "--chunk", "200")
        self.assertEqual(code, 0, out)
        d = os.path.join(self.work, "out", "studio")
        files = sorted(x for x in os.listdir(d) if x.startswith("load-"))
        self.assertGreater(len(files), 1)
        with open(os.path.join(d, files[-1]), encoding="utf-8") as f:
            code_text = f.read()
        self.assertIn("SetEntries", code_text)
        code, out = run(self.work, "studio", "verify")
        self.assertEqual(code, 0, out)
        self.assertTrue(os.path.exists(os.path.join(d, "verify-01.luau")))


if __name__ == "__main__":
    unittest.main()
