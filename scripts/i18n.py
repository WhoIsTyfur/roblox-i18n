#!/usr/bin/env python3
# roblox-i18n helper: locale sets, ingest, planning, merge, lint, export.
# Copyright (c) 2026 Tyler Fursman. SPDX-License-Identifier: MIT
import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
import unicodedata

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALES_FILE = os.path.join(SKILL_DIR, "data", "locales.json")
BATCH_SIZE = 150
# One analyst writes about 460 bytes of context per string, all in one file.
CONTEXT_PART = 150
CSV_MAX_CHANGED = 1000
CSV_MAX_ENTRIES = 10000
CSV_MAX_BYTES = 2 * 1024 * 1024
META_COLUMNS = ("key", "source", "context", "example", "location")
DECISIONS = ("translate", "keep", "transliterate")
SEVERITIES = ("minor", "major", "critical")
# Number specifiers take a Lua number; FormatByKey output for them is locale-formatted.
NUMBER_SPECS = ("int", "fixed", "num", "hex", "datetime", "iso8601", "shorttime", "shortdatetime", "shortdate")
ALIASES = {
    "brazilian": "pt-br", "brazilian portuguese": "pt-br", "european portuguese": "pt-pt",
    "latin american spanish": "es-mx", "latam spanish": "es-mx", "mexican spanish": "es-mx", "es-419": "es-mx",
    "castilian": "es-es", "european spanish": "es-es", "british english": "en-gb", "uk english": "en-gb",
    "american english": "en-us", "canadian french": "fr-ca", "quebec french": "fr-ca",
    "tagalog": "fil-ph", "myanmar": "my-mm", "cambodian": "km-kh", "sinhalese": "si-lk",
}

LANG_COL_RE = re.compile(r"^[a-z]{2,3}(-[a-z0-9]{2,4})?$")
PARAM_RE = re.compile(r"\{[^{}]*\}")
TAG_RE = re.compile(r"<\s*(/?)\s*([A-Za-z]+)[^<>]*?(/?)>")
# A key that reads as an identifier (hud.reel, shop_buy, buyButton), not as a plain word.
KEYISH_RE = re.compile(r"[._:/-]|[a-z][A-Z]|\d")

SIMPLIFIED_ONLY = set(
    "这个们时间级买卖宠币奖励设关开让说请进还选择输码无过满宝龙点击战剑欢组队务动线经验场东车门问题页钱头发现实体机会来对从张长号数当双获胜败赢购礼积为与"
    "听见觉认识读写语话谁吗应该网络连续标图钥锁宽岛乐园鸟鱼马鸡猪声乐边远运输赛团结终胜爱灵护药剂炼铁铜银钻杀杂级")
TRADITIONAL_ONLY = set(
    "這個們時間級買賣寵幣獎勵設關開讓說請進還選擇輸碼無過滿寶龍點擊戰鬥劍歡組隊務動線經驗場東車門問題頁錢頭發現實體機會來對從張長號數當雙獲勝敗贏購禮積為與"
    "聽見覺認識讀寫語話誰嗎應該網絡連續標圖鑰鎖寬島樂園鳥魚馬雞豬聲邊遠運輸賽團結終愛靈護藥劑煉鐵銅銀鑽殺雜")
SCRIPT_NAMES = {
    "Latn": ("LATIN",),
    "Cyrl": ("CYRILLIC",),
    "Arab": ("ARABIC",),
    "Grek": ("GREEK",),
    "Hans": ("CJK",),
    "Hant": ("CJK",),
    "Jpan": ("HIRAGANA", "KATAKANA", "CJK"),
    "Kore": ("HANGUL", "CJK"),
    "Thai": ("THAI",),
    "Deva": ("DEVANAGARI",),
    "Beng": ("BENGALI",),
    "Mymr": ("MYANMAR",),
    "Khmr": ("KHMER",),
    "Sinh": ("SINHALA",),
    "Geor": ("GEORGIAN",),
}
ZAWGYI_RE = re.compile(r"(^|[\s၊။])ေ[က-အ]|ဳ|ဴ|[ၠ-႗]")


class Fail(Exception):
    pass


# ---------- io ----------

def read_json(path, default=None):
    if not os.path.exists(path):
        if default is not None:
            return default
        raise Fail("missing file: " + path)
    try:
        with open(path, encoding="utf-8-sig") as f:
            return json.load(f)
    except ValueError as e:
        raise Fail("invalid JSON in %s: %s" % (path, e))


def json_object(path, default=None):
    data = read_json(path, default)
    if not isinstance(data, dict):
        raise Fail("%s must hold a JSON object" % path)
    return data


def preview(items, limit=8):
    items = list(items)
    return ", ".join(str(i) for i in items[:limit]) + (" ... (%d more)" % (len(items) - limit) if len(items) > limit else "")


def write_json(path, data):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def write_text(path, text):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def out(text=""):
    sys.stdout.buffer.write((text + "\n").encode("utf-8"))


# ---------- locales ----------

def load_locales():
    return read_json(LOCALES_FILE)["locales"]


def locale_by_id(locales):
    return {l["id"]: l for l in locales}


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c)).strip()


def words(s):
    return set(re.findall(r"\w+", norm(s)))


def resolve_single(target, locales):
    t = norm(target).replace("_", "-")
    t = ALIASES.get(t, t)
    exact = [l for l in locales if l["id"] == t]
    if exact:
        return exact
    found = []
    for l in locales:
        names = {norm(l["name"]), norm(l["name"].split(" (")[0]), norm(l["native"]),
                 norm(l["native"].split(" (")[0]), l["code"]}
        if l["code"].startswith("zh"):
            names.add("zh")
        if t in names:
            found.append(l)
    if not found:
        # "simplified chinese", "norwegian": every word of the ask appears in the name.
        found = [l for l in locales if words(t) and words(t) <= words(l["name"])]
    if not found:
        raise Fail("unknown language or locale: %s (try `locales all`)" % target)
    return found


def target_locales(mode, target, source_locale, locales):
    if mode == "single":
        if not target:
            raise Fail("single mode needs a language or locale, e.g. `single spanish`")
        chosen = resolve_single(target, locales)
    elif mode == "main":
        chosen = [l for l in locales if l["tier"] == "main"]
    elif mode == "all":
        chosen = list(locales)
    else:
        raise Fail("mode must be single, main or all")
    return [l for l in chosen if l["id"] != source_locale]


def column_for(loc):
    return loc["id"]


def bare_columns(targets, source_locale, locales):
    """Bare language columns (es, pt, fr, en) for languages with several Roblox locales."""
    target_ids = {l["id"] for l in targets}
    involved = target_ids | {source_locale}
    result = {}
    for l in locales:
        if l.get("default") and l["id"] in involved and any(
                x["code"] == l["code"] and x["id"] in target_ids for x in locales):
            result[l["code"]] = l["id"]
    return result


# ---------- work dir ----------

class Work:
    def __init__(self, root):
        self.root = root

    def p(self, *parts):
        return os.path.join(self.root, *parts)

    def loc(self, locale, *parts):
        return self.p("locales", locale, *parts)

    def config(self):
        return read_json(self.p("config.json"), {})

    def source(self):
        return read_json(self.p("source.json"))

    def existing(self):
        return read_json(self.p("existing.json"), {})

    def state(self):
        return read_json(self.p("state.json"), {})

    def context(self):
        return read_json(self.p("context.json"), {"strings": {}})

    def glossary(self):
        return read_json(self.p("glossary.json"), {"terms": []})

    def batches(self, locale):
        return numbered(self.loc(locale), r"batch-(\d+)\.todo\.json$")

    def batch(self, locale, n, kind):
        return self.loc(locale, "batch-%02d.%s.json" % (n, kind))

    def parts(self):
        return numbered(self.p("context"), r"part-(\d+)\.in\.json$")

    def part(self, n, kind):
        return self.p("context", "part-%02d.%s.json" % (n, kind))


def numbered(folder, pattern):
    if not os.path.isdir(folder):
        return []
    found = (re.match(pattern, name) for name in os.listdir(folder))
    return sorted(int(m.group(1)) for m in found if m)


def shash(source, context):
    return hashlib.sha1((source + "\x1f" + (context or "")).encode("utf-8")).hexdigest()[:12]


def entry_id(key, source, context=""):
    # Roblox identifies an entry with no Key by Source plus Context.
    if key:
        return key
    return source + " | " + context if context else source


def is_keyless(s):
    # Work folders from before the flag existed can only guess from Key == Source.
    return s.get("keyless", s["key"] == s["source"])


def blind_ids(keys):
    # Keys name the English ("hud.reel"), so the back-translator gets ids that say nothing.
    return {k: "s%03d" % i for i, k in enumerate(keys, 1)}


# ---------- csv ----------

def sniff_csv(path):
    with open(path, "rb") as f:
        raw = f.read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    newline = "\r\n" if "\r\n" in text else "\n"
    return text, bom, newline


def read_csv(path):
    text, bom, newline = sniff_csv(path)
    rows = list(csv.reader(io.StringIO(text, newline="")))
    if not rows:
        raise Fail("empty csv: " + path)
    header = rows[0]
    lower = [h.strip().lower() for h in header]
    if "source" not in lower:
        raise Fail("csv has no Source column: " + path)
    body = []
    for r in rows[1:]:
        if not any(c.strip() for c in r):
            continue
        r = r + [""] * (len(header) - len(r))
        body.append(r)
    return {"header": header, "lower": lower, "rows": body, "bom": bom, "newline": newline}


def write_csv(path, header, rows, bom=False, newline="\n"):
    buf = io.StringIO(newline="")
    w = csv.writer(buf, lineterminator=newline)
    w.writerow(header)
    for r in rows:
        w.writerow(r)
    data = buf.getvalue().encode("utf-8")
    if bom:
        data = b"\xef\xbb\xbf" + data
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    return len(data)


# ---------- commands ----------

def cmd_locales(a):
    locales = load_locales()
    targets = target_locales(a.mode, a.target, a.source, locales)
    for l in targets:
        out("%-7s %-8s %-26s %s" % (l["id"], l["tier"], l["name"], l["native"]))
    out("%d target locales (source %s)" % (len(targets), a.source))


def ingest_rows(work, source_locale, rows_meta, adapter, path):
    strings, existing = [], {}
    seen = set()
    for key, source, context, example, values, location in rows_meta:
        if not source:
            continue
        eid = entry_id(key, source, context)
        if eid in seen:
            raise Fail("duplicate entry %r: Roblox needs a unique Key, or a unique Source+Context "
                       "for entries with no Key" % eid)
        seen.add(eid)
        item = {"key": eid, "source": source, "context": context, "example": example,
                "hash": shash(source, context), "keyless": not key}
        if location:
            item["location"] = location
        strings.append(item)
        vals = {c: v for c, v in values.items() if isinstance(v, str) and v.strip()}
        if vals:
            existing[eid] = vals
    write_json(work.p("source.json"), {"source_locale": source_locale, "strings": strings})
    write_json(work.p("existing.json"), existing)
    cfg = work.config()
    cfg.update({"source_locale": source_locale, "adapter": adapter, "path": os.path.abspath(path) if path else None})
    write_json(work.p("config.json"), cfg)
    out("ingested %d strings, %d with existing translations" % (len(strings), len(existing)))


def cmd_ingest(a):
    work = Work(a.work)
    if a.kind == "csv":
        c = read_csv(a.paths[0])
        idx = {name: c["lower"].index(name) for name in META_COLUMNS if name in c["lower"]}
        lang_cols = [(i, h.strip().lower()) for i, h in enumerate(c["header"])
                     if c["lower"][i] not in META_COLUMNS and LANG_COL_RE.match(c["lower"][i])]
        rows = []
        for r in c["rows"]:
            g = lambda n: r[idx[n]] if n in idx else ""
            rows.append((g("key"), g("source"), g("context"), g("example"), {col: r[i] for i, col in lang_cols},
                         g("location")))
        ingest_rows(work, a.source.lower(), rows, "rojo" if a.rojo else "csv", a.paths[0])
    elif a.kind == "studio":
        rows, source_locale, table = [], a.source, None
        for path in a.paths:
            d = read_json(path)
            source_locale = (d.get("sourceLocaleId") or source_locale).lower()
            table = d.get("table", table)
            for e in d.get("entries", []):
                rows.append((e.get("Key") or "", e.get("Source") or "", e.get("Context") or "",
                             e.get("Example") or "", {k.lower(): v for k, v in (e.get("Values") or {}).items()}, ""))
        ingest_rows(work, source_locale, rows, "studio", None)
        cfg = work.config()
        cfg["table"] = table
        write_json(work.p("config.json"), cfg)
    else:
        raise Fail("ingest kind must be csv or studio")


def existing_for(existing_vals, loc, locales_by_id):
    if loc["id"] in existing_vals:
        return existing_vals[loc["id"]]
    if loc.get("default") and loc["code"] in existing_vals:
        return existing_vals[loc["code"]]
    return None


def archive(d, prefix):
    """Move a finished or abandoned run's files to history/NNN so no later command re-reads them."""
    if not os.path.isdir(d):
        return
    files = [f for f in os.listdir(d) if f.startswith(prefix)]
    if not files:
        return
    n = 1
    while os.path.exists(os.path.join(d, "history", "%03d" % n)):
        n += 1
    dest = os.path.join(d, "history", "%03d" % n)
    os.makedirs(dest)
    for f in files:
        os.replace(os.path.join(d, f), os.path.join(dest, f))


def cmd_plan(a):
    work = Work(a.work)
    locales = load_locales()
    lbi = locale_by_id(locales)
    src = work.source()
    source_locale = src["source_locale"]
    targets = target_locales(a.mode, a.target, source_locale, locales)
    if a.batch < 1:
        raise Fail("--batch must be 1 or more")
    existing, state = work.existing(), work.state()
    plan = {"mode": a.mode, "target": a.target, "source_locale": source_locale,
            "locales": [l["id"] for l in targets], "batches": {}}
    src_keys = {s["key"] for s in src["strings"]}
    total_batches = runs = 0
    planned = set()
    for loc in targets:
        final_path = work.loc(loc["id"], "final.json")
        final = read_json(final_path, {})
        # A string deleted from the game would otherwise sit in final.json and fail lint forever.
        if any(k not in src_keys for k in final):
            final = {k: v for k, v in final.items() if k in src_keys}
            write_json(final_path, final)
        todo, audit = [], []
        for s in src["strings"]:
            k = s["key"]
            ex = existing_for(existing.get(k, {}), loc, lbi)
            ours = state.get(k, {}).get(loc["id"])
            done_here = final.get(k, {}).get("source_hash") == s["hash"]
            if a.retranslate:
                todo.append(k)
            elif done_here:
                continue
            elif ex is None:
                todo.append(k)
            elif ours is not None and ours != s["hash"]:
                todo.append(k)
            elif ours is None and a.audit:
                audit.append(k)
        new_todos = []
        for mode, keys in (("translate", todo), ("audit", audit)):
            for i in range(0, len(keys), a.batch):
                new_todos.append({"locale": loc["id"], "batch": len(new_todos) + 1,
                                  "keys": keys[i:i + a.batch], "mode": mode})
        old = [read_json(work.batch(loc["id"], m, "todo")) for m in work.batches(loc["id"])]
        if old != new_todos:
            archive(work.loc(loc["id"]), "batch-")
            for t in new_todos:
                write_json(work.batch(loc["id"], t["batch"], "todo"), t)
                if t["mode"] == "audit":
                    write_json(work.batch(loc["id"], t["batch"], "draft"),
                               {k: {"text": existing_for(existing[k], loc, lbi), "confidence": "unknown",
                                    "note": "existing translation under audit"} for k in t["keys"]})
        n = len(new_todos)
        plan["batches"][loc["id"]] = n
        total_batches += n
        for t in new_todos:
            runs += 3 if t["mode"] == "translate" else 2
            planned.update(t["keys"])
    write_json(work.p("plan.json"), plan)
    parts = write_parts(work)
    runs += len(parts)
    busy = [l for l in plan["locales"] if plan["batches"][l]]
    out("mode %s: %d locales, %d need work, %d batches" % (a.mode, len(targets), len(busy), total_batches))
    for l in busy:
        out("  %-7s %d batch(es)" % (l, plan["batches"][l]))
    out("agent runs: about %d (translator, back-translator, reviewer per batch; audit batches skip the "
        "translator; +1 per batch that needs a resolve round)" % runs)
    if parts:
        out("context analyst needed: %d string(s) have no context entry yet, in %d part(s) (counted above)"
            % (sum(parts.values()), len(parts)))
    report_parts(work, parts)


def planned_keys(work):
    plan = read_json(work.p("plan.json"))
    keys = []
    for l in plan["locales"]:
        for n in work.batches(l):
            keys += read_json(work.batch(l, n, "todo"))["keys"]
    return list(dict.fromkeys(keys))


def context_group(s):
    # One screen's strings should reach one analyst: same key prefix, or same captured object.
    if not is_keyless(s):
        return "key", re.split(r"[._:/-]", s["key"], maxsplit=1)[0]
    place = s.get("location") or s.get("context")
    return ("place", ".".join(place.split(".")[:2])) if place else ("alone", s["key"])


def split_context(strings, size):
    """Analyst parts of at most `size` keys, evenly loaded. A group that fits in one part is never cut."""
    if not strings:
        return []
    groups = {}
    for s in strings:
        groups.setdefault(context_group(s), []).append(s["key"])
    count = -(-len(strings) // size)
    target = -(-len(strings) // count)
    parts = []
    for g in groups.values():
        step = target if len(g) > size else len(g)
        for i in range(0, len(g), step):
            piece = g[i:i + step]
            home = next((p for p in parts if len(p) < target and len(p) + len(piece) <= size), None)
            if home is None:
                home = []
                parts.append(home)
            home.extend(piece)
    return parts


def write_parts(work, size=None):
    """Analyst inputs for the planned strings that lack context. Returns {part number: string count}."""
    if size is not None and size < 1:
        raise Fail("--part must be 1 or more")
    planned = set(planned_keys(work))
    ctx = json_object(work.p("context.json"), {"strings": {}})
    have = ctx.get("strings") if isinstance(ctx.get("strings"), dict) else {}
    todo = [s for s in work.source()["strings"] if s["key"] in planned and not isinstance(have.get(s["key"]), dict)]
    old = {n: read_json(work.part(n, "in")) for n in work.parts()}
    held = [list(p["strings"]) for p in old.values()]
    # Planning again must not throw away a split the analysts are already working on.
    if size is None and sorted(k for keys in held for k in keys) == sorted(s["key"] for s in todo):
        split = held
    else:
        split = split_context(todo, size or CONTEXT_PART)
    by_key = {s["key"]: s for s in todo}
    new = {}
    for n, keys in enumerate(split, 1):
        new[n] = {"part": n, "parts": len(split)}
        if isinstance(ctx.get("game"), dict) and ctx["game"]:
            new[n]["game"] = ctx["game"]
        new[n]["strings"] = {k: {f: by_key[k][f] for f in ("source", "context", "example", "location")
                                 if by_key[k].get(f)} for k in keys}
    if new != old:
        if split != held:
            archive(work.p("context"), "part-")
        for n, part in new.items():
            write_json(work.part(n, "in"), part)
    return {n: len(p["strings"]) for n, p in new.items()}


def whole_table_part(work):
    """True when one part holds every string, so its analyst can describe the game."""
    nums = work.parts()
    return len(nums) == 1 and len(read_json(work.part(nums[0], "in"))["strings"]) == len(work.source()["strings"])


def report_parts(work, parts):
    if parts and not whole_table_part(work) and not json_object(work.p("context.json"), {}).get("game"):
        out("no analyst will see the whole table: write the game block to context.json first, "
            "then run contextpack (SKILL.md step 4)")


def cmd_contextpack(a):
    work = Work(a.work)
    parts = write_parts(work, a.part)
    for n, count in parts.items():
        out("%s (%d strings)" % (work.part(n, "in"), count))
    out("contextpack: %d part(s), %d string(s) with no context entry yet" % (len(parts), sum(parts.values())))
    report_parts(work, parts)


def context_problems(key, c):
    found = []
    if not c.get("where") or not c.get("role"):
        found.append("%s: context needs both where and role" % key)
    mx = c.get("max")
    if mx is not None and (isinstance(mx, bool) or not isinstance(mx, (int, float)) or mx <= 0):
        found.append("%s: max must be a positive number or null, got %r" % (key, mx))
    return found


def term_problem(t):
    if not isinstance(t, dict) or not isinstance(t.get("term"), str) or not t["term"].strip():
        return "glossary entry without a term: %r" % (t,)
    if t.get("decision") not in DECISIONS:
        return "glossary term %r: decision must be translate, keep or transliterate" % t["term"]
    return None


def merge_terms(existing, proposals):
    """Add the parts' terms to the glossary. An existing term wins; parts that disagree are left to the user."""
    terms = list(existing)
    known = {t["term"] for t in terms if not term_problem(t)}
    added, views = {}, {}
    # Terms match by exact spelling: a promo code STARFALL and the word Starfall are two terms.
    for n, t in proposals:
        t = dict(t, term=t["term"].strip())
        if t["term"] in known:
            continue
        views.setdefault(t["term"], []).append((n, t))
        if t["term"] not in added:
            added[t["term"]] = t
            terms.append(t)
    conflicts = []
    for name, t in added.items():
        if len({v["decision"] for _, v in views[name]}) > 1:
            t["ask"] = True
            t["conflict"] = "; ".join(
                "part %d: %s%s" % (n, v["decision"], " (%s)" % v["reason"] if v.get("reason") else "")
                for n, v in views[name])
            conflicts.append(t)
    return terms, list(added.values()), conflicts


def merge_parts(work):
    """Fold the analysts' part files into context.json and glossary.json. Returns what stops it, if anything."""
    nums = work.parts()
    if not nums:
        return []
    ctx = json_object(work.p("context.json"), {"strings": {}})
    if not isinstance(ctx.get("strings"), dict):
        raise Fail('context.json needs a "strings" object keyed by string key')
    glossary = json_object(work.p("glossary.json"), {"terms": []})
    if not isinstance(glossary.get("terms"), list):
        raise Fail('glossary.json needs a "terms" list')
    problems, strings, proposals, game, merged = [], {}, [], None, 0
    for n in nums:
        keys = [k for k in read_json(work.part(n, "in"))["strings"] if not isinstance(ctx["strings"].get(k), dict)]
        if not keys:
            continue
        merged += 1
        cpath, gpath = work.part(n, "context"), work.part(n, "glossary")
        missing = [p for p in (cpath, gpath) if not os.path.exists(p)]
        if missing:
            problems.append("part %d: no %s yet: run the context analyst first" % (n, " or ".join(missing)))
            continue
        data = json_object(cpath)
        got = data.get("strings")
        if not isinstance(got, dict):
            problems.append('%s needs a "strings" object keyed by string key' % cpath)
            continue
        lacking = [k for k in keys if not isinstance(got.get(k), dict)]
        if lacking:
            problems.append("%s: %d string(s) have no context entry: %s" % (cpath, len(lacking), preview(lacking)))
        for k in keys:
            if isinstance(got.get(k), dict):
                problems += ["%s: %s" % (cpath, m) for m in context_problems(k, got[k])]
                strings[k] = got[k]
        if game is None and isinstance(data.get("game"), dict) and data["game"]:
            game = data["game"]
        terms = json_object(gpath).get("terms")
        if not isinstance(terms, list):
            problems.append('%s needs a "terms" list' % gpath)
            continue
        for t in terms:
            m = term_problem(t)
            if m:
                problems.append("%s: %s" % (gpath, m))
            else:
                proposals.append((n, t))
    if merged and not ctx.get("game") and not whole_table_part(work):
        # An analyst who read a slice of the table cannot say what the game is.
        problems.append("context.json has no game block, and no analyst saw the whole table: write it there "
                        "(title, genre, core_loop, audience, tone), then run pack again")
    elif merged and not ctx.get("game") and not game:
        problems.append("%s has no game block (title, genre, core_loop, audience, tone)"
                        % work.part(nums[0], "context"))
    if problems:
        return problems
    if merged:
        terms, added, conflicts = merge_terms(glossary["terms"], proposals)
        ctx["strings"].update(strings)
        ctx["game"] = ctx.get("game") or game
        write_json(work.p("context.json"), dict({"game": ctx["game"]}, **ctx))
        write_json(work.p("glossary.json"), dict(glossary, terms=terms))
        out("context: merged %d part(s): %d string(s), %d new glossary term(s)" % (merged, len(strings), len(added)))
        for t in conflicts:
            out("conflict %s: %s. Kept the first, marked ask" % (t["term"], t["conflict"]))
    archive(work.p("context"), "part-")
    return []


def param_names(text):
    return [p[1:-1].split(":")[0] for p in PARAM_RE.findall(text)]


def glossary_terms(work, decision=None):
    return [t["term"] for t in work.glossary().get("terms", [])
            if isinstance(t, dict) and isinstance(t.get("term"), str) and t["term"]
            and (decision is None or t.get("decision") == decision)]


def check_inputs(work, keys):
    """Problems in context.json and glossary.json that would repeat in every locale."""
    src = {s["key"]: s for s in work.source()["strings"]}
    if not os.path.exists(work.p("context.json")):
        raise Fail("no context.json yet: run the context analyst first")
    strings = json_object(work.p("context.json")).get("strings")
    if not isinstance(strings, dict):
        raise Fail('context.json needs a "strings" object keyed by string key')
    errors, warns = [], []
    missing = [k for k in keys if not isinstance(strings.get(k), dict)]
    if missing:
        errors.append("%d string(s) have no context entry: %s" % (len(missing), preview(missing)))
    for k in keys:
        c = strings.get(k)
        if not isinstance(c, dict):
            continue
        errors += context_problems(k, c)
        params = c.get("params") if isinstance(c.get("params"), dict) else {}
        unknown = sorted(n for n in set(param_names(src[k]["source"])) if n not in params)
        if unknown:
            warns.append("%s: no meaning or sample for {%s}" % (k, "}, {".join(unknown)))
    terms = work.glossary().get("terms")
    if not isinstance(terms, list):
        raise Fail('glossary.json needs a "terms" list')
    for t in terms:
        m = term_problem(t)
        if m:
            errors.append(m)
        elif t.get("conflict"):
            errors.append('glossary term %r: analysts disagreed (%s); settle its decision and delete "conflict"'
                          % (t["term"], t["conflict"]))
    asks = [t["term"] for t in terms if isinstance(t, dict) and t.get("ask")]
    if asks:
        warns.append("%d glossary term(s) still marked ask (checkpoint not done?): %s" % (len(asks), preview(asks)))
    return errors, warns


def current_translations(work, loc, src, skip):
    """What players already read in this locale, so new strings can match it."""
    final = read_json(work.loc(loc["id"], "final.json"), {})
    existing = work.existing()
    result = {}
    for k, s in src.items():
        if k in skip:
            continue
        f = final.get(k, {})
        if f.get("source_hash") == s["hash"] and f.get("text"):
            result[k] = f["text"]
        else:
            ex = existing_for(existing.get(k, {}), loc, None)
            if ex:
                result[k] = ex
    return result


def batch_pack(work, loc, todo, src, ctx, translated):
    strings = {}
    for k in todo["keys"]:
        s, c = src[k], ctx.get("strings", {}).get(k, {})
        item = {"source": s["source"]}
        for f in ("example", "location"):
            if s.get(f):
                item[f] = s[f]
        for f in ("where", "role", "max", "params", "notes"):
            if c.get(f) not in (None, "", {}, []):
                item[f] = c[f]
        near = []
        for nk in c.get("neighbors") or []:
            if nk in src and nk != k:
                n = {"key": nk, "source": src[nk]["source"]}
                if nk in translated:
                    n["translation"] = translated[nk]
                near.append(n)
        if near:
            item["neighbors"] = near
        strings[k] = item
    return {"locale": loc["id"], "locale_name": loc["name"], "batch": todo["batch"], "mode": todo["mode"],
            "game": ctx.get("game", {}), "strings": strings}


def pack_parts(work, locale):
    loc = locale_by_id(load_locales()).get(locale)
    if not loc:
        raise Fail("unknown locale " + locale)
    src = {s["key"]: s for s in work.source()["strings"]}
    todos = {n: read_json(work.batch(locale, n, "todo")) for n in work.batches(locale)}
    gone = [k for t in todos.values() for k in t["keys"] if k not in src]
    if gone:
        raise Fail("%s: planned key(s) no longer in source.json, run plan again: %s" % (locale, preview(gone)))
    skip = {k for t in todos.values() for k in t["keys"]}
    return loc, src, todos, current_translations(work, loc, src, skip)


def cmd_pack(a):
    work = Work(a.work)
    plan = read_json(work.p("plan.json"))
    locs = [l for l in plan["locales"] if work.batches(l)]
    keys = planned_keys(work)
    known = {s["key"] for s in work.source()["strings"]}
    unmerged = merge_parts(work)
    for m in unmerged:
        out("ERROR " + m)
    if unmerged and not os.path.exists(work.p("context.json")):
        raise Fail("fix what is named above, then run pack again")
    errors, warns = check_inputs(work, [k for k in keys if k in known])
    for m in warns:
        out("warn  " + m)
    for m in errors:
        out("ERROR " + m)
    if unmerged:
        raise Fail("fix what is named above, then run pack again")
    if errors:
        raise Fail("fix context.json or glossary.json, then run pack again")
    ctx = work.context()
    count = 0
    for l in locs:
        loc, src, todos, translated = pack_parts(work, l)
        for n, todo in todos.items():
            write_json(work.batch(l, n, "in"), batch_pack(work, loc, todo, src, ctx, translated))
            count += 1
    out("pack: %d batch input file(s) for %d locale(s), %d string(s) checked" % (count, len(locs), len(keys)))


def agent_object(path, wrapper, expected=(), default=None):
    """An agent's output file. Agents often copy the wrapper of their input around the entries; drop it."""
    data = json_object(path, default)
    inner = data.get(wrapper)
    if isinstance(inner, dict) and not any(k in data for k in expected):
        write_json(path, inner)
        out("note: %s had its entries under \"%s\"; rewrote it flat" % (path, wrapper))
        return inner
    return data


def load_terms(work, locale):
    path = work.loc(locale, "terms.json")
    terms = agent_object(path, "terms", default={})
    if any(not isinstance(v, str) for v in terms.values()):
        raise Fail('%s must be one flat object: {"glossary term": "rendering"}' % path)
    return terms


def load_draft(work, locale, n, todo):
    path = work.batch(locale, n, "draft")
    draft = agent_object(path, "strings", todo["keys"])
    bad = [k for k in todo["keys"] if not isinstance(draft.get(k), dict)
           or not isinstance(draft[k].get("text"), str) or not draft[k]["text"].strip()]
    if bad:
        raise Fail('%s: %d key(s) missing or without "text": %s' % (path, len(bad), preview(bad)))
    return draft


def load_back(work, locale, n, todo, required=True):
    path = work.batch(locale, n, "back")
    ids = blind_ids(todo["keys"])
    raw = agent_object(path, "strings", list(ids.values()) + todo["keys"], None if required else {})
    back = {}
    for k in todo["keys"]:
        v = raw.get(ids[k], raw.get(k))
        if isinstance(v, str) and v.strip():
            back[k] = v
    missing = [ids[k] for k in todo["keys"] if k not in back]
    if required and missing:
        raise Fail("%s: no back-translation for %d string(s): %s" % (path, len(missing), preview(missing)))
    return back


def load_review(work, locale, n, todo):
    path = work.batch(locale, n, "review")
    review = agent_object(path, "strings", todo["keys"])
    bad = []
    for k in todo["keys"]:
        r = review.get(k)
        if not isinstance(r, dict) or r.get("verdict") not in ("ok", "fix"):
            bad.append("%s (verdict must be ok or fix)" % k)
        elif r["verdict"] == "fix" and (not isinstance(r.get("text"), str) or not r["text"].strip()):
            bad.append("%s (a fix needs text)" % k)
        elif r["verdict"] == "fix" and r.get("severity") not in SEVERITIES:
            bad.append("%s (severity must be minor, major or critical)" % k)
    if bad:
        raise Fail("%s: %d bad entr%s: %s" % (path, len(bad), "y" if len(bad) == 1 else "ies", preview(bad)))
    return review


def scrub(where, hidden):
    for t in hidden:
        if not t:
            continue
        where = re.sub(r"(?<!\w)" + re.escape(t) + r"(?!\w)", "[name]", where, flags=re.I)
    return where


def cmd_backpack(a):
    work = Work(a.work)
    ctx = work.context().get("strings", {})
    todo = read_json(work.batch(a.locale, a.batch, "todo"))
    draft = load_draft(work, a.locale, a.batch, todo)
    load_terms(work, a.locale)
    strings = work.source()["strings"]
    src = {x["key"]: x["source"] for x in strings}
    hidden = [t for t in glossary_terms(work) if len(t) > 1]
    hidden +=[x["key"] for x in strings if not is_keyless(x) and KEYISH_RE.search(x["key"])]
    hidden.sort(key=len, reverse=True)
    ids = blind_ids(todo["keys"])
    pack = {}
    for k in todo["keys"]:
        c = ctx.get(k, {})
        # The blind reader must not see source wording, even inside the context note.
        where = scrub(c.get("where", ""), [src.get(k, "")] + hidden)
        pack[ids[k]] = {"text": draft[k]["text"], "role": c.get("role", ""), "where": where}
    write_json(work.batch(a.locale, a.batch, "backin"), pack)
    out("wrote %s (%d strings)" % (work.batch(a.locale, a.batch, "backin"), len(pack)))


def cmd_reviewpack(a):
    work = Work(a.work)
    todo = read_json(work.batch(a.locale, a.batch, "todo"))
    draft = load_draft(work, a.locale, a.batch, todo)
    back = load_back(work, a.locale, a.batch, todo)
    loc, src, todos, translated = pack_parts(work, a.locale)
    pack = batch_pack(work, loc, todo, src, work.context(), translated)
    report = lint_items(work, a.locale, {k: draft[k] for k in todo["keys"]})
    for k, item in pack["strings"].items():
        d = draft[k]
        item["text"] = d["text"]
        for f in ("note", "confidence", "keep"):
            if d.get(f):
                item[f] = d[f]
        item["back"] = back[k]
        e, w = report.get(k, ([], []))
        if e or w:
            item["lint"] = ["ERROR: " + m for m in e] + ["warn: " + m for m in w]
    path = work.batch(a.locale, a.batch, "reviewin")
    write_json(path, pack)
    flagged = sum(1 for i in pack["strings"].values() if i.get("lint"))
    out("wrote %s (%d strings, %d with lint findings)" % (path, len(pack["strings"]), flagged))


def visible(text):
    return TAG_RE.sub("", PARAM_RE.sub("", text))


def width(text):
    # Mn/Me marks take no space; Mc (Indic spacing vowel signs) does.
    return sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
               for c in visible(text) if unicodedata.category(c) not in ("Mn", "Me", "Cf"))


def tags(text):
    # Whole tag, so a translated or re-quoted attribute (<font color="rojo">) is caught too.
    return sorted(re.sub(r"\s+", "", m.group(0)).replace("'", '"').lower() for m in TAG_RE.finditer(text))


def digits(text):
    # Native digits count as their value, so an Arabic-Indic 50 matches "50".
    found = (unicodedata.digit(c, None) for c in visible(text))
    return sorted(str(d) for d in found if d is not None)


def is_latin(c):
    # NFKD turns the Spanish and Portuguese ordinal marks (U+00BA, U+00AA) into plain o and a.
    if unicodedata.category(c) == "Lm":
        return True
    return all(unicodedata.name(x, "").startswith("LATIN") for x in unicodedata.normalize("NFKD", c)
               if unicodedata.category(x).startswith("L"))


def letters_outside(text, terms):
    stripped = visible(text)
    for term in terms:
        stripped = term_re(term).sub("", stripped)
    return [c for c in stripped if unicodedata.category(c).startswith("L")]


def term_re(term, suffix=False):
    # Latin-only boundaries: \b would fail on "Robuxで" because CJK counts as a word character.
    tail = "" if suffix else r"(?![A-Za-z0-9])"
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term) + tail)


def has_term(text, term, suffix=False):
    return bool(term_re(term, suffix).search(text))


def lint_string(key, source, text, loc, item, ctx, keep_terms, src_lang_same, latin_terms=()):
    errors, warns = [], []
    if not isinstance(text, str) or not text.strip():
        return ["empty translation"], []
    if "�" in text or any(unicodedata.category(c) == "Cc" and c not in "\n\t" for c in text):
        errors.append("replacement or control character")
    if sorted(PARAM_RE.findall(source)) != sorted(PARAM_RE.findall(text)):
        errors.append("params differ: source %s, translation %s" %
                      (sorted(PARAM_RE.findall(source)), sorted(PARAM_RE.findall(text))))
    if tags(source) != tags(text):
        errors.append("rich-text tags differ: source %s, translation %s" % (tags(source), tags(text)))
    # "{count}", "100%" or a string made only of keep-terms has nothing to translate.
    if text == source and not item.get("keep") and not src_lang_same and letters_outside(source, keep_terms):
        errors.append("identical to source without keep:true")
    for term in keep_terms:
        # Case endings are allowed on the translation side (Estonian "Robuxi", Finnish "Robuxilla").
        if has_term(source, term) and not has_term(text, term, suffix=True):
            errors.append("keep-term %r missing" % term)
    letters = letters_outside(text, list(keep_terms) + list(latin_terms))
    want = SCRIPT_NAMES.get(loc.get("script", "Latn"), ("LATIN",))
    if letters and not item.get("keep"):
        ok = sum(1 for c in letters if unicodedata.name(c, "").startswith(want))
        if loc.get("script", "Latn") == "Latn":
            bad = [c for c in letters if not is_latin(c)]
            if bad:
                errors.append("non-Latin letters in a Latin-script locale: %s" % "".join(sorted(set(bad))[:10]))
        elif len(letters) >= 3 and ok / len(letters) < 0.5:
            errors.append("mostly not in %s script (%d of %d letters); if the Latin text is deliberate, "
                          "set keep:true and say why in note" % (loc["script"], ok, len(letters)))
    if loc["id"] == "zh-tw":
        leak = sorted({c for c in text if c in SIMPLIFIED_ONLY})
        if leak:
            errors.append("Simplified-only characters in zh-tw: %s" % "".join(leak))
    if loc["id"] == "zh-cn":
        leak = sorted({c for c in text if c in TRADITIONAL_ONLY})
        if leak:
            errors.append("Traditional-only characters in zh-cn: %s" % "".join(leak))
    if loc["id"] == "my-mm" and ZAWGYI_RE.search(text):
        errors.append("looks like Zawgyi encoding; Burmese must be Unicode")
    if loc["id"] == "ro-ro" and re.search("[ŞşŢţ]", text):
        errors.append("cedilla s/t; Romanian uses comma-below ș ț")
    if loc["id"] == "ka-ge" and re.search("[Ა-Ჿ]", text):
        errors.append("Mtavruli capitals; Georgian UI text uses Mkhedruli only")
    if (source[:1].isspace() != text[:1].isspace()) or (source[-1:].isspace() != text[-1:].isspace()):
        warns.append("leading/trailing whitespace differs from source")
    if "  " in text and "  " not in source:
        warns.append("double space")
    if digits(source) != digits(text) and not item.get("note"):
        warns.append("numbers differ from the source with no note: source %s, translation %s" %
                     ("".join(digits(source)) or "none", "".join(digits(text)) or "none"))
    mx = ctx.get("max")
    if isinstance(mx, (int, float)) and mx > 0:
        w = width(text)
        if w > 2 * mx:
            errors.append("length %d is over twice the budget %d" % (w, mx))
        elif w > mx and not item.get("note"):
            warns.append("length %d over budget %d with no note" % (w, mx))
    return errors, warns


def lint_items(work, locale, items, skip_unknown=False):
    locales = locale_by_id(load_locales())
    loc = locales.get(locale)
    if not loc:
        raise Fail("unknown locale " + locale)
    source = work.source()
    src = {s["key"]: s for s in source["strings"]}
    ctx = work.context().get("strings", {})
    keep_terms = glossary_terms(work, "keep")
    same = locales.get(source["source_locale"], {}).get("code") == loc["code"]
    latin_terms = [t for t, r in load_terms(work, locale).items() if r == t]
    report = {}
    for k, item in items.items():
        if k not in src:
            # A final.json entry for a string since deleted from the game is not shipped.
            if not skip_unknown:
                report[k] = (["key not in source.json"], [])
            continue
        if not isinstance(item, dict):
            report[k] = (["entry is not a JSON object"], [])
            continue
        c = ctx.get(k) if isinstance(ctx.get(k), dict) else {}
        e, w = lint_string(k, src[k]["source"], item.get("text"), loc, item, c, keep_terms, same, latin_terms)
        if e or w:
            report[k] = (e, w)
    return report


def lint_locale(work, locale, stage="final", quiet=False):
    if stage == "final":
        # needs_native strings are held back from export, so they cannot fail the gate.
        items = {k: v for k, v in read_json(work.loc(locale, "final.json"), {}).items()
                 if not (isinstance(v, dict) and v.get("status") == "needs_native")}
    else:
        items = {}
        for n in work.batches(locale):
            items.update(read_json(work.batch(locale, n, "draft"), {}))
    report = lint_items(work, locale, items, skip_unknown=stage == "final")
    if not quiet:
        for k, (e, w) in report.items():
            for m in e:
                out("%s %s ERROR %s" % (locale, k, m))
            for m in w:
                out("%s %s warn  %s" % (locale, k, m))
    return report


def cmd_lint(a):
    work = Work(a.work)
    plan = read_json(work.p("plan.json"), {"locales": []})
    locs = a.locales or [l for l in plan["locales"] if os.path.exists(work.loc(l, "final.json"))]
    errors = 0
    for l in locs:
        rep = lint_locale(work, l, a.stage)
        errors += sum(len(e) for e, _ in rep.values())
    out("lint: %d locale(s), %d error(s)" % (len(locs), errors))
    if errors:
        sys.exit(1)


def cmd_apply(a):
    work = Work(a.work)
    src = {s["key"]: s for s in work.source()["strings"]}
    final = {k: v for k, v in read_json(work.loc(a.locale, "final.json"), {}).items() if k in src}
    decisions = json_object(work.loc(a.locale, "decisions.json"), {})
    need_resolve, disputes = [], {}
    batches = work.batches(a.locale)
    if not batches:
        raise Fail("no batches for %s; run plan first" % a.locale)
    for n in batches:
        todo = read_json(work.batch(a.locale, n, "todo"))
        gone = [k for k in todo["keys"] if k not in src]
        if gone:
            raise Fail("%s: planned key(s) no longer in source.json, run plan again: %s" % (a.locale, preview(gone)))
        draft = load_draft(work, a.locale, n, todo)
        review = load_review(work, a.locale, n, todo)
        resolve = agent_object(work.batch(a.locale, n, "resolve"), "strings", todo["keys"], {}) if a.resolve else {}
        back = load_back(work, a.locale, n, todo, required=False)
        for k in todo["keys"]:
            d, r = draft[k], review[k]
            item = {"text": d.get("text"), "confidence": d.get("confidence", "unknown"),
                    "source_hash": src[k]["hash"], "status": "ok", "flags": []}
            if d.get("keep"):
                item["keep"] = True
            if d.get("note"):
                item["note"] = d["note"]
            remark = re.search(r"\[([^\[\]]+)\]\s*$", str(back.get(k, "")))
            if remark and r.get("verdict") != "fix":
                item["blind_remark"] = remark.group(1)
            if r.get("verdict") == "fix":
                if todo.get("mode") == "audit":
                    # The human translation this fix would replace, for the report.
                    item["was"] = d["text"]
                item["text"] = r.get("text") or item["text"]
                item["status"] = "fixed"
                if r.get("keep"):
                    item["keep"] = True
                sev = r.get("severity", "minor")
                item["flags"].append("review:%s:%s" % (sev, r.get("category", "")))
                item["review_reason"] = r.get("reason", "")
                if sev in ("major", "critical"):
                    need_resolve.append(k)
            if k in resolve:
                res = resolve[k]
                if not isinstance(res, dict) or not (res.get("accept") is True or (
                        isinstance(res.get("text"), str) and res["text"].strip())):
                    raise Fail('%s: %s needs {"accept": true} or a "text"' % (work.batch(a.locale, n, "resolve"), k))
                if res.get("keep"):
                    item["keep"] = True
                if r.get("verdict") != "fix":
                    # Lint-only resolve: no reviewer text to dispute, so the translator's answer stands.
                    item["text"] = res.get("text") or item["text"]
                    item["status"] = "resolved"
                elif res.get("accept"):
                    item["status"] = "resolved"
                else:
                    item["status"] = "disputed"
                    disputes[k] = {"source": src[k]["source"], "draft": d.get("text"), "reviewer": r.get("text"),
                                   "reviewer_reason": r.get("reason"), "translator": res.get("text"),
                                   "translator_reason": res.get("reason")}
                if k in need_resolve:
                    need_resolve.remove(k)
            if k in decisions:
                dec = decisions[k]
                if not isinstance(dec, dict) or not (dec.get("needs_native") or (
                        isinstance(dec.get("text"), str) and dec["text"].strip())):
                    raise Fail('%s: %s needs a "text" or "needs_native": true' % (work.loc(a.locale, "decisions.json"), k))
                if dec.get("text"):
                    item["text"] = dec["text"]
                if dec.get("keep"):
                    item["keep"] = True
                item["status"] = "needs_native" if dec.get("needs_native") else "decided"
                item["decision_reason"] = dec.get("reason", "")
                disputes.pop(k, None)
                if k in need_resolve:
                    need_resolve.remove(k)
            final[k] = item
    write_json(work.loc(a.locale, "final.json"), final)
    if disputes:
        write_json(work.loc(a.locale, "disputes.json"), disputes)
    elif os.path.exists(work.loc(a.locale, "disputes.json")):
        os.remove(work.loc(a.locale, "disputes.json"))
    rep = lint_locale(work, a.locale, "final", quiet=True)
    lint_keys = [k for k, (e, _) in rep.items() if e]
    out("%s: %d strings in final.json" % (a.locale, len(final)))
    for k, (e, w) in rep.items():
        for m in e:
            out("  ERROR %s: %s" % (k, m))
        for m in w:
            out("  warn  %s: %s" % (k, m))
    todo_resolve = sorted(set(need_resolve) | set(lint_keys))
    if todo_resolve and not a.resolve:
        out("resolve round needed for %d key(s): %s" % (len(todo_resolve), ", ".join(todo_resolve)))
    elif todo_resolve:
        out("still failing after resolve: %s. Decide in decisions.json" % ", ".join(todo_resolve))
    if disputes:
        out("%d dispute(s) in disputes.json. Decide each in decisions.json, then apply again" % len(disputes))
    if not todo_resolve and not disputes:
        out("clean")


def merged_values(work, targets, bare):
    finals = {l: read_json(work.loc(l, "final.json"), {}) for l in targets}
    src = {s["key"]: s for s in work.source()["strings"]}
    values = {}
    for l, fin in finals.items():
        for k, item in fin.items():
            if k in src and item.get("source_hash") == src[k]["hash"] and item.get("status") != "needs_native":
                values.setdefault(k, {})[l] = item["text"]
    source_locale = work.source()["source_locale"]
    lbi = locale_by_id(load_locales())
    for code, default_id in bare.items():
        for k, s in src.items():
            vals = values.get(k, {})
            if default_id == source_locale:
                if any(lbi[l]["code"] == code for l in vals if l in lbi):
                    vals[code] = s["source"]
                    vals[source_locale] = s["source"]
            elif default_id in vals:
                vals[code] = vals[default_id]
    return values


def language_values(values, locales):
    lbi = locale_by_id(locales)
    result = {}
    for k, vals in values.items():
        for l, text in vals.items():
            loc = lbi.get(l)
            if not loc:
                continue
            row = result.setdefault(k, {})
            if loc.get("default") or loc["code"] not in row:
                row[loc["code"]] = text
    return result


def cmd_export(a):
    work = Work(a.work)
    locales = load_locales()
    lbi = locale_by_id(locales)
    plan = read_json(work.p("plan.json"))
    src_strings = work.source()["strings"]
    source_locale = work.source()["source_locale"]
    targets = [l for l in plan["locales"] if os.path.exists(work.loc(l, "final.json"))]
    tlocs = [lbi[l] for l in targets]
    bare = bare_columns(tlocs, source_locale, locales) if a.columns == "locale" else {}
    values = merged_values(work, targets, bare)
    if a.columns == "language":
        values = language_values(values, locales)
    if a.kind == "csv":
        export_csv(work, a, values, src_strings, locales)
    elif a.kind == "studio":
        export_studio(work, a, values, src_strings, source_locale)
    else:
        raise Fail("export kind must be csv or studio")
    state = work.state()
    for l in targets:
        for k, item in read_json(work.loc(l, "final.json"), {}).items():
            if item.get("status") != "needs_native":
                state.setdefault(k, {})[l] = item.get("source_hash")
    write_json(work.p("state.json"), state)


def column_order(locales):
    order = []
    for l in locales:
        if l["code"] not in order:
            order.append(l["code"])
        order.append(l["id"])
    return {c: i for i, c in enumerate(order)}


def csv_size(row, newline):
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator=newline).writerow(row)
    return len(buf.getvalue().encode("utf-8"))


def split_parts(header, rows, newline):
    """Upload files that each stay under Roblox's changed-row and file-size limits."""
    budget = CSV_MAX_BYTES - 4096
    head = csv_size(header, newline)
    parts, cur, size = [], [], head
    for r in rows:
        n = csv_size(r, newline)
        if cur and (len(cur) >= CSV_MAX_CHANGED or size + n > budget):
            parts.append(cur)
            cur, size = [], head
        cur.append(r)
        size += n
    parts.append(cur)
    return parts


def export_csv(work, a, values, src_strings, locales):
    cfg = work.config()
    base_path = a.rojo or cfg.get("path")
    if base_path and os.path.exists(base_path) and cfg.get("adapter") in ("csv", "rojo"):
        c = read_csv(base_path)
        header, rows, bom, newline = list(c["header"]), [list(r) for r in c["rows"]], c["bom"], c["newline"]
    else:
        header = ["Key", "Source", "Context", "Example"]
        rows = [["" if is_keyless(s) else s["key"], s["source"], s["context"], s["example"]] for s in src_strings]
        bom, newline = False, "\n"
    lower = [h.strip().lower() for h in header]
    order = column_order(locales)
    new_cols = sorted({c for vals in values.values() for c in vals if c not in lower},
                      key=lambda c: (order.get(c, len(order)), c))
    for col in new_cols:
        header.append(col)
        lower.append(col)
        for r in rows:
            r.append("")
    ki, si = lower.index("key") if "key" in lower else None, lower.index("source")
    ci = lower.index("context") if "context" in lower else None
    changed = set()
    for i, r in enumerate(rows):
        r += [""] * (len(header) - len(r))
        eid = entry_id(r[ki] if ki is not None else "", r[si], r[ci] if ci is not None else "")
        for col, text in values.get(eid, {}).items():
            j = lower.index(col)
            if r[j] != text:
                r[j] = text
                changed.add(i)
    if len(rows) > CSV_MAX_ENTRIES:
        out("warning: %d entries is over Roblox's %d-entry table limit" % (len(rows), CSV_MAX_ENTRIES))
    if a.rojo:
        size = write_csv(a.rojo, header, rows, bom, newline)
        out("rewrote %s: %d rows, %d changed, %d bytes" % (a.rojo, len(rows), len(changed), size))
        return
    outp = a.out or work.p("out", "translations.csv")
    stem, ext = os.path.splitext(outp)
    parts = split_parts(header, [rows[i] for i in sorted(changed)], newline)
    for n, part in enumerate(parts, 1):
        path = outp if len(parts) == 1 else "%s-part%d%s" % (stem, n, ext)
        size = write_csv(path, header, part, bom, newline)
        warn = " (over Roblox's 2 MB upload limit)" if size > CSV_MAX_BYTES else ""
        out("wrote %s: %d changed rows, %d bytes%s" % (path, len(part), size, warn))
    out("upload each file in Creator Hub > Localization > your table > Update/Upload CSV")


LUAU_LOAD = """local HttpService = game:GetService("HttpService")
local ChangeHistoryService = game:GetService("ChangeHistoryService")
local LocalizationService = game:GetService("LocalizationService")
local data = HttpService:JSONDecode([%(eq)s[%(json)s]%(eq)s])
local recording = ChangeHistoryService:TryBeginRecording("roblox-i18n chunk %(n)d")
local function id(key, source, context)
	return if key ~= "" then "k\\31" .. key else "s\\31" .. source .. "\\31" .. (context or "")
end
-- pcall so a failed chunk still closes its recording; an open one blocks every later recording.
local ok, result = pcall(function()
	local tbl = LocalizationService:FindFirstChild(%(table)s)
	if not tbl then
		tbl = Instance.new("LocalizationTable")
		tbl.Name = %(table)s
		tbl.SourceLocaleId = %(source)s
		tbl.Parent = LocalizationService
	end
	local entries = tbl:GetEntries()
	local index = {}
	for i, e in entries do
		index[id(e.Key or "", e.Source, e.Context)] = i
	end
	local added, updated = 0, 0
	for _, d in data do
		local i = index[id(d.key, d.source, d.context)]
		if i then
			for loc, text in d.values do
				entries[i].Values[loc] = text
			end
			updated += 1
		else
			table.insert(entries, { Key = d.key, Source = d.source, Context = d.context, Example = d.example, Values = d.values })
			index[id(d.key, d.source, d.context)] = #entries
			added += 1
		end
	end
	tbl:SetEntries(entries)
	return string.format("chunk %(n)d: %%d updated, %%d added, %%d entries in %%s", updated, added, #entries, tbl.Name)
end)
if recording then
	ChangeHistoryService:FinishRecording(
		recording,
		if ok then Enum.FinishRecordingOperation.Commit else Enum.FinishRecordingOperation.Cancel
	)
end
if not ok then
	error(result, 0)
end
return result
"""


def luau_str(s):
    return json.dumps(s, ensure_ascii=False)


def long_bracket(payload):
    n = 1
    while ("]" + "=" * n + "]") in payload:
        n += 1
    return "=" * n


def export_studio(work, a, values, src_strings, source_locale):
    table = a.table or work.config().get("table") or "GameStrings"
    payload = []
    for s in src_strings:
        if s["key"] in values:
            key = "" if is_keyless(s) else s["key"]
            payload.append({"key": key, "source": s["source"], "context": s["context"], "example": s["example"],
                            "values": values[s["key"]]})
    chunks, cur = [], []
    for item in payload:
        cur.append(item)
        if len(json.dumps(cur, ensure_ascii=False)) > a.chunk:
            if len(cur) > 1:
                cur.pop()
                chunks.append(cur)
                cur = [item]
            else:
                chunks.append(cur)
                cur = []
    if cur:
        chunks.append(cur)
    outdir = work.p("out", "studio")
    os.makedirs(outdir, exist_ok=True)
    for name in os.listdir(outdir):
        if name.startswith("load-") and name.endswith(".luau"):
            os.remove(os.path.join(outdir, name))
    for n, chunk in enumerate(chunks, 1):
        js = json.dumps(chunk, ensure_ascii=False)
        code = LUAU_LOAD % {"eq": long_bracket(js), "json": js, "table": luau_str(table), "n": n,
                            "source": luau_str(source_locale)}
        write_text(os.path.join(outdir, "load-%02d.luau" % n), code)
    out("wrote %d Luau chunk(s) to %s for table %s (%d entries)" % (len(chunks), outdir, table, len(payload)))
    out("run each with execute_luau in Edit mode, in order; then run `i18n.py studio verify`")


STUDIO_DUMP = """local HttpService = game:GetService("HttpService")
local LocalizationService = game:GetService("LocalizationService")
local OFFSET, LIMIT = %(offset)d, %(limit)d
local tables = {}
for _, t in LocalizationService:GetDescendants() do
	if t:IsA("LocalizationTable") then
		table.insert(tables, t:GetFullName())
	end
end
local tbl = LocalizationService:FindFirstChild(%(table)s)
if not tbl then
	return HttpService:JSONEncode({ tables = tables, missing = %(table)s })
end
local all = tbl:GetEntries()
local page = {}
for i = OFFSET + 1, math.min(OFFSET + LIMIT, #all) do
	table.insert(page, all[i])
end
return HttpService:JSONEncode({ table = tbl.Name, sourceLocaleId = tbl.SourceLocaleId, total = #all,
	offset = OFFSET, tables = tables, entries = page })
"""

STUDIO_VERIFY = """local LocalizationService = game:GetService("LocalizationService")
local HttpService = game:GetService("HttpService")
local cases = HttpService:JSONDecode([%(eq)s[%(json)s]%(eq)s])
local result = {}
for loc, list in cases do
	local ok, tr = pcall(LocalizationService.GetTranslatorForLocaleAsync, LocalizationService, loc)
	local r = { throws = 0, mismatches = {}, checked = 0 }
	if not ok then
		r.error = tostring(tr)
	else
		for _, c in list do
			local ok2, v = pcall(tr.FormatByKey, tr, c.key, c.args)
			r.checked += 1
			if not ok2 then
				r.throws += 1
				table.insert(r.mismatches, { key = c.key, error = tostring(v) })
			elseif c.expect and v ~= c.expect then
				table.insert(r.mismatches, { key = c.key, got = v, expect = c.expect })
			end
		end
	end
	result[loc] = r
end
return HttpService:JSONEncode(result)
"""


def as_number(sample):
    try:
        n = float(str(sample).replace(",", ""))
    except ValueError:
        return 1
    return int(n) if n == int(n) else n


def fill(text, args):
    def rep(m):
        name = m.group(0)[1:-1].split(":")[0]
        return str(args.get(name, m.group(0)))
    return PARAM_RE.sub(rep, text)


def cmd_studio(a):
    work = Work(a.work)
    table = a.table or work.config().get("table") or "GameStrings"
    if a.action == "dump":
        out(STUDIO_DUMP % {"offset": a.offset, "limit": a.limit, "table": luau_str(table)})
        return
    plan = read_json(work.p("plan.json"))
    ctx = work.context().get("strings", {})
    src = {s["key"]: s for s in work.source()["strings"]}
    locs = [l for l in plan["locales"] if os.path.exists(work.loc(l, "final.json"))]
    locs += [x for x in a.extra.split(",") if x] if a.extra else []
    lbi = locale_by_id(load_locales())
    cases_all = {}
    for l in locs:
        base = l if l in lbi else next((x for x in plan["locales"] if lbi[x]["code"] == l.split("-")[0]
                                        and lbi[x].get("default")), None)
        fin = read_json(work.loc(base, "final.json"), {}) if base else {}
        cases = []
        for k, item in fin.items():
            if (k not in src or is_keyless(src[k]) or item.get("source_hash") != src[k]["hash"]
                    or item.get("status") == "needs_native"):
                continue
            specs = {}
            for p in PARAM_RE.findall(item["text"]):
                name, _, spec = p[1:-1].partition(":")
                specs[name] = spec.lower()
            params = ctx.get(k, {}).get("params") if isinstance(ctx.get(k), dict) else None
            args = {}
            for name, spec in specs.items():
                sample = params.get(name) if isinstance(params, dict) else None
                if isinstance(sample, dict):
                    sample = sample.get("sample")
                if isinstance(sample, bool) or not isinstance(sample, (str, int, float)):
                    sample = None
                if spec in NUMBER_SPECS:
                    args[name] = as_number(sample)
                else:
                    # A Lua number in a plain {param} renders as 99.00, so samples go in as strings.
                    args[name] = "X" if sample is None else str(sample)
            case = {"key": k, "args": args}
            # A specifier formats per locale, so only a throw can be checked there.
            if not any(specs.values()):
                case["expect"] = fill(item["text"], args)
            cases.append(case)
        cases_all[l] = cases
    outdir = work.p("out", "studio")
    os.makedirs(outdir, exist_ok=True)
    names = sorted(cases_all)
    for i in range(0, len(names), a.per):
        group = {n: cases_all[n] for n in names[i:i + a.per]}
        js = json.dumps(group, ensure_ascii=False)
        path = os.path.join(outdir, "verify-%02d.luau" % (i // a.per + 1))
        write_text(path, STUDIO_VERIFY % {"eq": long_bracket(js), "json": js})
        out("wrote " + path)


def cmd_status(a):
    work = Work(a.work)
    src = work.source()
    existing = work.existing()
    out("source %s: %d strings" % (src["source_locale"], len(src["strings"])))
    counts = {}
    for vals in existing.values():
        for c in vals:
            counts[c] = counts.get(c, 0) + 1
    if counts:
        out("existing translations: " + ", ".join("%s %d" % (c, n) for c, n in sorted(counts.items())))
    plan = read_json(work.p("plan.json"), {})
    if not plan:
        return
    parts = ["p%d:%s" % (n, "+".join(k for k in ("in", "context", "glossary") if os.path.exists(work.part(n, k))))
             for n in work.parts()]
    if parts:
        out("  context %s (pack merges them)" % " ".join(parts))
    for l in plan["locales"]:
        row = []
        for n in work.batches(l):
            have = [k for k in ("in", "draft", "backin", "back", "reviewin", "review", "resolve")
                    if os.path.exists(work.batch(l, n, k))]
            row.append("b%d:%s" % (n, "+".join(have) or "todo"))
        fin = read_json(work.loc(l, "final.json"), {})
        out("  %-7s %s final=%d" % (l, " ".join(row) or "-", len(fin)))


def cmd_check(a):
    """Lint the values actually written to an exported CSV against its Source column."""
    work = Work(a.work)
    locales = load_locales()
    lbi = locale_by_id(locales)
    by_code = {l["code"]: l for l in locales if l.get("default")}
    by_code.update({l["code"]: l for l in locales if sum(1 for x in locales if x["code"] == l["code"]) == 1})
    keep = glossary_terms(work, "keep")
    src_locale = work.config().get("source_locale", "en-us")
    hashes = {s["key"]: s["hash"] for s in work.source()["strings"]}
    finals = {}
    c = read_csv(a.path)
    lower = c["lower"]
    si, ki = lower.index("source"), (lower.index("key") if "key" in lower else None)
    ci = lower.index("context") if "context" in lower else None
    errors = checked = mismatched = 0
    for r in c["rows"]:
        eid = entry_id(r[ki] if ki is not None else "", r[si], r[ci] if ci is not None else "")
        for j, col in enumerate(lower):
            if col in META_COLUMNS or not r[j].strip():
                continue
            loc = lbi.get(col) or by_code.get(col)
            if not loc:
                continue
            checked += 1
            same = lbi.get(src_locale, {}).get("code") == loc["code"]
            if loc["id"] not in finals:
                finals[loc["id"]] = read_json(work.loc(loc["id"], "final.json"), {})
            fin = finals[loc["id"]].get(eid, {})
            e, _ = lint_string(eid, r[si], r[j], loc, {"keep": fin.get("keep") or r[j] == r[si]}, {}, keep, same)
            for m in e:
                errors += 1
                out("%s %s ERROR %s" % (col, eid, m))
            # Only what export would write: a held-back or outdated final.json entry is not in the file.
            shipped = fin.get("source_hash") == hashes.get(eid) and fin.get("status") != "needs_native"
            if col == loc["id"] and shipped and fin.get("text") != r[j]:
                mismatched += 1
                out("%s %s differs from final.json" % (col, eid))
    out("check: %d values, %d error(s), %d differ from final.json" % (checked, errors, mismatched))
    if errors or mismatched:
        sys.exit(1)


def cmd_report(a):
    work = Work(a.work)
    lbi = locale_by_id(load_locales())
    plan = read_json(work.p("plan.json"))
    src = {s["key"]: s for s in work.source()["strings"]}
    lines = ["# roblox-i18n report", "",
             "Source %s, %d strings, mode %s." % (plan["source_locale"], len(src), plan["mode"]), "",
             "| Locale | Strings | Fixed by review | Disputed / native | Lint errors | Confidence high/med/low | Native review | Render risk |",
             "|---|---|---|---|---|---|---|---|"]
    detail = []
    for l in plan["locales"]:
        fin = read_json(work.loc(l, "final.json"), {})
        if not fin:
            lines.append("| %s | not done | | | | | | |" % l)
            continue
        rep = lint_locale(work, l, "final", quiet=True)
        errs = sum(len(e) for e, _ in rep.values())
        st = [i.get("status") for i in fin.values()]
        conf = [i.get("confidence") for i in fin.values()]
        loc = lbi[l]
        flagged = [k for k, i in fin.items() if i.get("status") in ("disputed", "needs_native")
                   or i.get("confidence") == "low"]
        second = [k for k, i in fin.items() if i.get("blind_remark") and k not in flagged
                  and not i.get("keep")]
        lines.append("| %s | %d | %d | %d | %d | %d/%d/%d | %s | %s |" % (
            l, len(fin), st.count("fixed") + st.count("resolved") + st.count("decided"),
            st.count("disputed") + st.count("needs_native"), errs,
            conf.count("high"), conf.count("medium"), conf.count("low"),
            loc.get("native_review", "?"), loc.get("render_risk", "?")))
        if flagged or second:
            detail.append("## %s: for a native speaker" % l)
            for k in flagged:
                i = fin[k]
                detail.append("- `%s`: %s -> %s (%s)" % (k, src.get(k, {}).get("source", ""), i.get("text"),
                                                       i.get("status") + (", " + i.get("review_reason", "") if i.get("review_reason") else "")))
            if second:
                detail.append("")
                detail.append("Flagged by the blind back-translator, passed by the reviewer:")
                for k in second:
                    i = fin[k]
                    detail.append("- `%s`: %s -> %s (%s)" % (k, src.get(k, {}).get("source", ""), i.get("text"),
                                                            i["blind_remark"]))
            detail.append("")
        replaced = [k for k, i in fin.items() if i.get("was") and i.get("was") != i.get("text")]
        if replaced:
            detail.append("## %s: changes to existing translations" % l)
            for k in replaced:
                i = fin[k]
                detail.append("- `%s`: %s: %s -> %s (%s)" % (k, src.get(k, {}).get("source", ""), i["was"],
                                                            i.get("text"), i.get("review_reason", "")))
            detail.append("")
    risky = [l for l in plan["locales"] if lbi[l].get("render_risk") in ("medium", "high")]
    if risky:
        detail.append("## Rendering risks")
        for l in risky:
            detail.append("- %s (%s): %s" % (l, lbi[l]["render_risk"], lbi[l].get("render_note", "")))
        detail.append("")
    audit = work.p("audit.md")
    if os.path.exists(audit):
        with open(audit, encoding="utf-8") as fh:
            body = fh.read().strip().splitlines()
        detail.append("## Localizability audit")
        detail.extend(body[1:] if body and body[0].startswith("# ") else body)
        detail.append("")
    text = "\n".join(lines + [""] + detail)
    write_text(work.p("report.md"), text)
    out(text)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="i18n.py", description="roblox-i18n helper")
    ap.add_argument("--work", default=".roblox-i18n", help="work folder (default .roblox-i18n)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("locales", help="print the target locales for a mode")
    s.add_argument("mode", choices=["single", "main", "all"])
    s.add_argument("target", nargs="?")
    s.add_argument("--source", default="en-us")
    s.set_defaults(fn=cmd_locales)

    s = sub.add_parser("ingest", help="read strings from a CSV or Studio dump")
    s.add_argument("kind", choices=["csv", "studio"])
    s.add_argument("paths", nargs="+")
    s.add_argument("--rojo", action="store_true", help="the CSV is a Rojo LocalizationTable in the repo")
    s.add_argument("--source", default="en-us", help="source locale of the table")
    s.set_defaults(fn=cmd_ingest)

    s = sub.add_parser("status", help="show strings, existing translations and batch progress")
    s.set_defaults(fn=cmd_status)

    s = sub.add_parser("plan", help="choose what to translate and write batch files")
    s.add_argument("mode", choices=["single", "main", "all"])
    s.add_argument("target", nargs="?")
    s.add_argument("--retranslate", action="store_true")
    s.add_argument("--audit", action="store_true", help="review existing translations not made by this tool")
    s.add_argument("--batch", type=int, default=BATCH_SIZE)
    s.set_defaults(fn=cmd_plan)

    s = sub.add_parser("contextpack", help="split the strings with no context into analyst parts (plan does it too)")
    s.add_argument("--part", type=int, help="strings per part (default %d)" % CONTEXT_PART)
    s.set_defaults(fn=cmd_contextpack)

    s = sub.add_parser("pack", help="merge the analysts' parts, check context.json and glossary.json, "
                                    "then write each batch's translator input")
    s.set_defaults(fn=cmd_pack)

    s = sub.add_parser("backpack", help="write the blind input for the back-translator")
    s.add_argument("locale")
    s.add_argument("batch", type=int)
    s.set_defaults(fn=cmd_backpack)

    s = sub.add_parser("reviewpack", help="join source, context, draft, back-translation and lint for the reviewer")
    s.add_argument("locale")
    s.add_argument("batch", type=int)
    s.set_defaults(fn=cmd_reviewpack)

    s = sub.add_parser("apply", help="merge draft + review (+ resolve, decisions) into final.json and lint")
    s.add_argument("locale")
    s.add_argument("--resolve", action="store_true")
    s.set_defaults(fn=cmd_apply)

    s = sub.add_parser("lint", help="check translations")
    s.add_argument("locales", nargs="*")
    s.add_argument("--stage", choices=["final", "draft"], default="final")
    s.set_defaults(fn=cmd_lint)

    s = sub.add_parser("export", help="write translations out")
    s.add_argument("kind", choices=["csv", "studio"])
    s.add_argument("--out", help="CSV path for Creator Hub upload files")
    s.add_argument("--rojo", help="rewrite this Rojo CSV in place")
    s.add_argument("--columns", choices=["locale", "language"], default="locale",
                   help="locale: one column per locale plus bare default columns; language: language codes only")
    s.add_argument("--table", help="LocalizationTable name under LocalizationService (studio)")
    s.add_argument("--chunk", type=int, default=60000, help="max JSON characters per Luau chunk")
    s.set_defaults(fn=cmd_export)

    s = sub.add_parser("studio", help="Luau snippets: dump a table, or verify loaded translations")
    s.add_argument("action", choices=["dump", "verify"])
    s.add_argument("--table")
    s.add_argument("--offset", type=int, default=0)
    s.add_argument("--limit", type=int, default=400)
    s.add_argument("--extra", default="es-419,fr-be,pt-ao", help="extra fallback locales to check")
    s.add_argument("--per", type=int, default=6, help="locales per verify snippet")
    s.set_defaults(fn=cmd_studio)

    s = sub.add_parser("check", help="lint the values in an exported CSV without touching the work folder")
    s.add_argument("path")
    s.set_defaults(fn=cmd_check)

    s = sub.add_parser("report", help="write report.md")
    s.set_defaults(fn=cmd_report)

    a = ap.parse_args(argv)
    try:
        a.fn(a)
    except Fail as e:
        sys.stderr.write("error: %s\n" % e)
        sys.exit(2)


if __name__ == "__main__":
    main()
