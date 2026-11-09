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
        run(self.work, "plan", "single", "es-mx", "--audit")
        self.assertFalse(os.path.exists(self.loc("es-mx", "batch-03.todo.json")))
        audit = read(self.loc("es-mx", "batch-02.todo.json"))
        self.assertEqual(audit["mode"], "audit")
        self.assertEqual(read(self.loc("es-mx", "batch-02.draft.json"))["shop.buy"]["text"], "Comprar")


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

    def test_width_counts_spacing_marks(self):
        self.assertEqual(i18n.width("खरीदें"), 4)
        self.assertEqual(i18n.width("{n} <b>購入</b>"), 5)


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
