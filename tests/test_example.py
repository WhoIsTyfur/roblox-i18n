import filecmp
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = os.path.join(ROOT, "scripts", "i18n.py")
EXAMPLE = os.path.join(ROOT, "examples", "lantern-lake")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


class ExampleReplayTest(unittest.TestCase):
    """The recorded Lantern Lake run must give the same result through today's tool."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.copy = os.path.join(self.tmp, "lantern-lake")
        shutil.copytree(EXAMPLE, self.copy)
        self.work = os.path.join(self.copy, "work")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_tool(self, *args):
        p = subprocess.run([sys.executable, TOOL, "--work", self.work] + list(args), capture_output=True,
                           cwd=ROOT, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        return p.returncode, (p.stdout + p.stderr).decode("utf-8")

    def test_replay(self):
        locales = sorted(os.listdir(os.path.join(self.work, "locales")))
        self.assertEqual(len(locales), 49)
        for locale in locales:
            folder = os.path.join(self.work, "locales", locale)
            recorded = load(os.path.join(folder, "final.json"))
            os.remove(os.path.join(folder, "final.json"))
            resolved = any(name.endswith(".resolve.json") for name in os.listdir(folder))
            code, out = self.run_tool("apply", locale, *(["--resolve"] if resolved else []))
            self.assertEqual(code, 0, out)
            self.assertIn("clean", out, locale)
            self.assertEqual(load(os.path.join(folder, "final.json")), recorded, locale)
        code, out = self.run_tool("lint")
        self.assertEqual(code, 0, out)
        self.assertNotIn(" warn ", out)
        outp = os.path.join(self.tmp, "translated.csv")
        code, out = self.run_tool("export", "csv", "--out", outp)
        self.assertEqual(code, 0, out)
        self.assertTrue(filecmp.cmp(outp, os.path.join(EXAMPLE, "translated.csv"), shallow=False))
        code, out = self.run_tool("check", outp)
        self.assertEqual(code, 0, out)
        code, out = self.run_tool("report")
        self.assertEqual(code, 0)
        with open(os.path.join(EXAMPLE, "work", "report.md"), encoding="utf-8") as f:
            self.assertEqual(out.replace("\r\n", "\n").strip(), f.read().strip())


if __name__ == "__main__":
    unittest.main()
