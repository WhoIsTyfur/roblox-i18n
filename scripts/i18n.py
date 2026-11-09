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
CSV_MAX_CHANGED = 1000
CSV_MAX_ENTRIES = 10000
CSV_MAX_BYTES = 2 * 1024 * 1024
META_COLUMNS = ("key", "source", "context", "example")

LANG_COL_RE = re.compile(r"^[a-z]{2,3}(-[a-z0-9]{2,4})?$")
PARAM_RE = re.compile(r"\{[^{}]*\}")
TAG_RE = re.compile(r"<\s*(/?)\s*([A-Za-z]+)[^<>]*?(/?)>")

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
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


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


def resolve_single(target, locales):
    t = norm(target)
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
        d = self.loc(locale)
        if not os.path.isdir(d):
            return []
        nums = []
        for name in os.listdir(d):
            m = re.match(r"batch-(\d+)\.todo\.json$", name)
            if m:
                nums.append(int(m.group(1)))
        return sorted(nums)

    def batch(self, locale, n, kind):
        return self.loc(locale, "batch-%02d.%s.json" % (n, kind))


def shash(source, context):
    return hashlib.sha1((source + "\x1f" + (context or "")).encode("utf-8")).hexdigest()[:12]


def entry_id(key, source):
    return key if key else source


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
    for key, source, context, example, values in rows_meta:
        if not source:
            continue
        eid = entry_id(key, source)
        if eid in seen:
            raise Fail("duplicate entry %r: Roblox requires unique Key and unique Source+Context" % eid)
        seen.add(eid)
        strings.append({"key": eid, "source": source, "context": context, "example": example,
                        "hash": shash(source, context)})
        vals = {c: v for c, v in values.items() if v.strip()}
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
            rows.append((g("key"), g("source"), g("context"), g("example"), {col: r[i] for i, col in lang_cols}))
        ingest_rows(work, a.source, rows, "rojo" if a.rojo else "csv", a.paths[0])
    elif a.kind == "studio":
        rows, source_locale, table = [], a.source, None
        for path in a.paths:
            d = read_json(path)
            source_locale = (d.get("sourceLocaleId") or source_locale).lower()
            table = d.get("table", table)
            for e in d.get("entries", []):
                rows.append((e.get("Key", ""), e.get("Source", ""), e.get("Context", ""), e.get("Example", ""),
                             {k.lower(): v for k, v in (e.get("Values") or {}).items()}))
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


def archive_batches(work, locale):
    """Move a finished or abandoned run's batch files to history/NNN so apply never re-reads them."""
    d = work.loc(locale)
    if not os.path.isdir(d):
        return
    files = [f for f in os.listdir(d) if f.startswith("batch-")]
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
    existing, state = work.existing(), work.state()
    plan = {"mode": a.mode, "target": a.target, "source_locale": source_locale,
            "locales": [l["id"] for l in targets], "batches": {}}
    total_batches = 0
    for loc in targets:
        final = read_json(work.loc(loc["id"], "final.json"), {})
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
            archive_batches(work, loc["id"])
            for t in new_todos:
                write_json(work.batch(loc["id"], t["batch"], "todo"), t)
                if t["mode"] == "audit":
                    write_json(work.batch(loc["id"], t["batch"], "draft"),
                               {k: {"text": existing_for(existing[k], loc, lbi), "confidence": "unknown",
                                    "note": "existing translation under audit"} for k in t["keys"]})
        n = len(new_todos)
        plan["batches"][loc["id"]] = n
        total_batches += n
    write_json(work.p("plan.json"), plan)
    runs = total_batches * 3 + (1 if total_batches else 0)
    busy = [l for l in plan["locales"] if plan["batches"][l]]
    out("mode %s: %d locales, %d need work, %d batches" % (a.mode, len(targets), len(busy), total_batches))
    for l in busy:
        out("  %-7s %d batch(es)" % (l, plan["batches"][l]))
    out("agent runs: about %d (context analyst + translator, back-translator, reviewer per batch; "
        "+1 per batch that needs a resolve round)" % runs)


def cmd_backpack(a):
    work = Work(a.work)
    ctx = work.context().get("strings", {})
    todo = read_json(work.batch(a.locale, a.batch, "todo"))
    draft = read_json(work.batch(a.locale, a.batch, "draft"))
    src = {x["key"]: x["source"] for x in work.source()["strings"]}
    terms = sorted((t["term"] for t in work.glossary().get("terms", []) if len(t["term"]) > 1), key=len, reverse=True)
    pack = {}
    for k in todo["keys"]:
        c = ctx.get(k, {})
        where = c.get("where", "")
        # The blind reader must not see source wording, even inside the context note.
        for t in [src.get(k, "")] + terms:
            if t:
                where = re.sub(re.escape(t), "[name]", where, flags=re.I)
        pack[k] = {"text": draft.get(k, {}).get("text", ""), "role": c.get("role", ""), "where": where}
    write_json(work.batch(a.locale, a.batch, "backin"), pack)
    out("wrote %s (%d strings)" % (work.batch(a.locale, a.batch, "backin"), len(pack)))


def visible(text):
    return TAG_RE.sub("", PARAM_RE.sub("", text))


def width(text):
    # Mn/Me marks take no space; Mc (Indic spacing vowel signs) does.
    return sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
               for c in visible(text) if unicodedata.category(c) not in ("Mn", "Me", "Cf"))


def tags(text):
    return sorted((m.group(1) + m.group(2).lower()) for m in TAG_RE.finditer(text))


def term_re(term, suffix=False):
    # Latin-only boundaries: \b would fail on "Robuxで" because CJK counts as a word character.
    tail = "" if suffix else r"(?![A-Za-z0-9])"
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term) + tail)


def has_term(text, term, suffix=False):
    return bool(term_re(term, suffix).search(text))


def lint_string(key, source, text, loc, item, ctx, keep_terms, src_lang_same, latin_terms=()):
    errors, warns = [], []
    if text is None or not str(text).strip():
        return ["empty translation"], []
    if "�" in text or any(unicodedata.category(c) == "Cc" and c not in "\n\t" for c in text):
        errors.append("replacement or control character")
    if sorted(PARAM_RE.findall(source)) != sorted(PARAM_RE.findall(text)):
        errors.append("params differ: source %s, translation %s" %
                      (sorted(PARAM_RE.findall(source)), sorted(PARAM_RE.findall(text))))
    if tags(source) != tags(text):
        errors.append("rich-text tags differ: source %s, translation %s" % (tags(source), tags(text)))
    if text == source and not item.get("keep") and not src_lang_same:
        errors.append("identical to source without keep:true")
    for term in keep_terms:
        # Case endings are allowed on the translation side (Estonian "Robuxi", Finnish "Robuxilla").
        if has_term(source, term) and not has_term(text, term, suffix=True):
            errors.append("keep-term %r missing" % term)
    stripped = visible(text)
    for term in list(keep_terms) + list(latin_terms):
        stripped = term_re(term).sub("", stripped)
    letters = [c for c in stripped if unicodedata.category(c).startswith("L")]
    want = SCRIPT_NAMES.get(loc.get("script", "Latn"), ("LATIN",))
    if letters and not item.get("keep"):
        ok = sum(1 for c in letters if unicodedata.name(c, "").startswith(want))
        if loc.get("script", "Latn") == "Latn":
            bad = [c for c in letters if not unicodedata.name(c, "").startswith("LATIN")]
            if bad:
                errors.append("non-Latin letters in a Latin-script locale: %s" % "".join(sorted(set(bad))[:10]))
        elif len(letters) >= 3 and ok / len(letters) < 0.5:
            errors.append("mostly not in %s script (%d of %d letters)" % (loc["script"], ok, len(letters)))
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
    mx = ctx.get("max")
    if isinstance(mx, (int, float)) and mx > 0:
        w = width(text)
        if w > 2 * mx:
            errors.append("length %d is over twice the budget %d" % (w, mx))
        elif w > mx and not item.get("note"):
            warns.append("length %d over budget %d with no note" % (w, mx))
    return errors, warns


def lint_locale(work, locale, stage="final", quiet=False):
    locales = locale_by_id(load_locales())
    loc = locales.get(locale)
    if not loc:
        raise Fail("unknown locale " + locale)
    src = {s["key"]: s for s in work.source()["strings"]}
    ctx = work.context().get("strings", {})
    keep_terms = [t["term"] for t in work.glossary().get("terms", []) if t.get("decision") == "keep"]
    src_locale = work.source()["source_locale"]
    same = locales.get(src_locale, {}).get("code") == loc["code"]
    terms = read_json(work.loc(locale, "terms.json"), {})
    latin_terms = [t for t, r in terms.items() if r == t]
    if stage == "final":
        items = read_json(work.loc(locale, "final.json"), {})
    else:
        items = {}
        for n in work.batches(locale):
            items.update(read_json(work.batch(locale, n, "draft"), {}))
    report = {}
    for k, item in items.items():
        if k not in src:
            report[k] = (["key not in source.json"], [])
            continue
        e, w = lint_string(k, src[k]["source"], item.get("text"), loc, item, ctx.get(k, {}), keep_terms, same,
                           latin_terms)
        if e or w:
            report[k] = (e, w)
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
    final = read_json(work.loc(a.locale, "final.json"), {})
    decisions = read_json(work.loc(a.locale, "decisions.json"), {})
    need_resolve, disputes = [], {}
    batches = work.batches(a.locale)
    if not batches:
        raise Fail("no batches for %s; run plan first" % a.locale)
    for n in batches:
        todo = read_json(work.batch(a.locale, n, "todo"))
        draft = read_json(work.batch(a.locale, n, "draft"))
        review = read_json(work.batch(a.locale, n, "review"))
        resolve = read_json(work.batch(a.locale, n, "resolve"), {}) if a.resolve else {}
        back = read_json(work.batch(a.locale, n, "back"), {})
        for k in todo["keys"]:
            if k not in draft:
                raise Fail("%s batch %d: draft is missing key %s" % (a.locale, n, k))
            if k not in review:
                raise Fail("%s batch %d: review is missing key %s" % (a.locale, n, k))
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
                item["text"] = r.get("text") or item["text"]
                item["status"] = "fixed"
                sev = r.get("severity", "minor")
                item["flags"].append("review:%s:%s" % (sev, r.get("category", "")))
                item["review_reason"] = r.get("reason", "")
                if sev in ("major", "critical"):
                    need_resolve.append(k)
            if k in resolve:
                res = resolve[k]
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
                if dec.get("text"):
                    item["text"] = dec["text"]
                item["status"] = "needs_native" if dec.get("needs_native") else "decided"
                item["decision_reason"] = dec.get("reason", "")
                disputes.pop(k, None)
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
        if l["code"] not in order and any(x["code"] == l["code"] and x.get("default") for x in locales):
            order.append(l["code"])
        order.append(l["id"])
    return {c: i for i, c in enumerate(order)}


def export_csv(work, a, values, src_strings, locales):
    cfg = work.config()
    base_path = a.rojo or cfg.get("path")
    if base_path and os.path.exists(base_path) and cfg.get("adapter") in ("csv", "rojo"):
        c = read_csv(base_path)
        header, rows, bom, newline = list(c["header"]), [list(r) for r in c["rows"]], c["bom"], c["newline"]
    else:
        header = ["Key", "Source", "Context", "Example"]
        rows = [[s["key"], s["source"], s["context"], s["example"]] for s in src_strings]
        bom, newline = False, "\n"
    lower = [h.strip().lower() for h in header]
    new_cols = sorted({c for vals in values.values() for c in vals if c not in lower},
                      key=lambda c: column_order(locales).get(c, 999))
    for col in new_cols:
        header.append(col)
        lower.append(col)
        for r in rows:
            r.append("")
    ki, si = lower.index("key") if "key" in lower else None, lower.index("source")
    changed = set()
    for i, r in enumerate(rows):
        r += [""] * (len(header) - len(r))
        eid = entry_id(r[ki] if ki is not None else "", r[si])
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
    changed_rows = [rows[i] for i in sorted(changed)]
    parts = [changed_rows[i:i + CSV_MAX_CHANGED] for i in range(0, len(changed_rows), CSV_MAX_CHANGED)] or [[]]
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
local tbl = LocalizationService:FindFirstChild(%(table)s)
local recording = ChangeHistoryService:TryBeginRecording("roblox-i18n chunk %(n)d")
if not tbl then
	tbl = Instance.new("LocalizationTable")
	tbl.Name = %(table)s
	tbl.SourceLocaleId = %(source)s
	tbl.Parent = LocalizationService
end
local entries = tbl:GetEntries()
local index = {}
local function id(key, source, context)
	return if key ~= "" then "k\\31" .. key else "s\\31" .. source .. "\\31" .. (context or "")
end
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
if recording then
	ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
end
return string.format("chunk %(n)d: %%d updated, %%d added, %%d entries in %%s", updated, added, #entries, tbl.Name)
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
            key = s["key"] if s["key"] != s["source"] else ""
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
            if k not in src or src[k]["key"] == src[k]["source"]:
                continue
            args = {}
            for name in [p[1:-1].split(":")[0] for p in PARAM_RE.findall(src[k]["source"])]:
                sample = ctx.get(k, {}).get("params", {}).get(name)
                if isinstance(sample, dict):
                    sample = sample.get("sample")
                args[name] = sample if isinstance(sample, (str, int, float)) else "X"
            cases.append({"key": k, "args": args, "expect": fill(item["text"], args)})
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
    for l in plan["locales"]:
        row = []
        for n in work.batches(l):
            have = [k for k in ("draft", "backin", "back", "review", "resolve") if os.path.exists(work.batch(l, n, k))]
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
    keep = [t["term"] for t in work.glossary().get("terms", []) if t.get("decision") == "keep"]
    src_locale = work.config().get("source_locale", "en-us")
    c = read_csv(a.path)
    lower = c["lower"]
    si, ki = lower.index("source"), (lower.index("key") if "key" in lower else None)
    errors = checked = mismatched = 0
    for r in c["rows"]:
        eid = entry_id(r[ki] if ki is not None else "", r[si])
        for j, col in enumerate(lower):
            if col in META_COLUMNS or not r[j].strip():
                continue
            loc = lbi.get(col) or by_code.get(col)
            if not loc:
                continue
            checked += 1
            same = lbi.get(src_locale, {}).get("code") == loc["code"]
            fin = read_json(work.loc(loc["id"], "final.json"), {}).get(eid, {})
            e, _ = lint_string(eid, r[si], r[j], loc, {"keep": fin.get("keep") or r[j] == r[si]}, {}, keep, same)
            for m in e:
                errors += 1
                out("%s %s ERROR %s" % (col, eid, m))
            if col == loc["id"] and fin and fin.get("text") != r[j]:
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
            l, len(fin), st.count("fixed") + st.count("resolved"),
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

    s = sub.add_parser("backpack", help="write the blind input for the back-translator")
    s.add_argument("locale")
    s.add_argument("batch", type=int)
    s.set_defaults(fn=cmd_backpack)

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
