import json
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDES = os.path.join(ROOT, "references", "locales")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import i18n  # noqa: E402

CELL = re.compile(r"(?<!\\)\|")


def text_of(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def headings(text):
    return re.findall(r"^## .+$", text, flags=re.M)


def reference_rows(text):
    section = text.split("## Reference translations", 1)[1].split("\n## ", 1)[0]
    rows = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in CELL.split(line)[1:-1]]
        if len(cells) < 2 or cells[0].lower() == "key" or set(cells[0]) <= set("-: "):
            continue
        value = cells[1]
        if len(value) > 1 and value.startswith("`") and value.endswith("`"):
            value = value[1:-1]
        rows[cells[0].strip("`")] = (value, cells[2] if len(cells) > 2 else "")
    return rows


class GuideTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.locales = i18n.load_locales()
        with open(os.path.join(ROOT, "references", "canonical-strings.json"), encoding="utf-8") as f:
            cls.canon = {s["key"]: s for s in json.load(f)["strings"]}

    def test_one_guide_per_locale(self):
        files = sorted(f[:-3] for f in os.listdir(GUIDES) if f.endswith(".md") and not f.startswith("_"))
        self.assertEqual(files, sorted(l["id"] for l in self.locales))

    def test_guides_keep_the_template_headings(self):
        want = headings(text_of(os.path.join(GUIDES, "_TEMPLATE.md")))
        self.assertEqual(len(want), 10)
        for l in self.locales:
            self.assertEqual(headings(text_of(os.path.join(GUIDES, l["id"] + ".md"))), want, l["id"])

    def test_reference_translations_pass_lint(self):
        problems = []
        for l in self.locales:
            rows = reference_rows(text_of(os.path.join(GUIDES, l["id"] + ".md")))
            if sorted(rows) != sorted(self.canon):
                problems.append("%s: rows differ from canonical-strings.json: %s" % (
                    l["id"], sorted(set(rows) ^ set(self.canon))))
            for key, (value, note) in rows.items():
                s = self.canon.get(key)
                if not s:
                    continue
                # A noted all-ASCII row is a deliberate Latin label, like BGM in Japanese.
                item = {"note": note, "keep": value == s["source"] or bool(note and value.isascii())}
                e, w = i18n.lint_string(key, s["source"], value, l, item, {"max": s.get("max")},
                                        ["Robux", "Pet Hatch Tycoon"], l["code"] == "en")
                problems += ["%s %s: %s" % (l["id"], key, m) for m in e + w]
        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
