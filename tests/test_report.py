import contextlib
import io
import os
import tempfile
import unittest

from indus.report import DISCLAIMER, main

FIX = os.path.join(os.path.dirname(__file__), "fixtures")
ARGS = ["--corpus", os.path.join(FIX, "tiny_corpus.json"),
        "--readings", os.path.join(FIX, "readings_dir"), "--n", "50"]
SKIP = "Skipped Mismatched test reading: sign_list M77 does not match corpus SYNTH"


class ReportTest(unittest.TestCase):
    def check(self, text):
        lines = text.splitlines()
        self.assertIn("Corpus: synthetic test fixture", lines)
        self.assertIn("License: CC0", lines)
        self.assertIn("Inscriptions: 8", lines)
        self.assertIn(DISCLAIMER, lines)
        header = "| name | author | year | coverage_tokens | coverage_types | " \
                 "full_inscriptions | consistency | repeat_agreement | " \
                 "lexicon_hits | null_mean | p_value |"
        self.assertIn(header, lines)
        rows = [l for l in lines if l.startswith("| ") and l != header]
        self.assertEqual(len(rows), 1)
        cells = [c.strip() for c in rows[0].strip("|").split("|")]
        self.assertEqual(cells[:7], ["Synthetic test reading", "Night Shift fixture", "2026",
                                     "0.731", "0.600", "0.250", "1.000"])
        self.assertEqual(cells[7:9], ["1.000", "5"])
        self.assertIn(SKIP, lines)

    def test_out_file(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "report.md")
            self.assertEqual(main(ARGS + ["--out", out]), 0)
            with open(out, encoding="utf-8") as f:
                self.check(f.read())

    def test_stdout(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(main(ARGS), 0)
        self.check(buf.getvalue())


if __name__ == "__main__":
    unittest.main()
