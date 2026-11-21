"""Tests for indus.manifest on synthetic fixtures in a temporary directory."""

import io
import json
import os
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout

from indus import manifest as m

SEMANTICS = {
    "sequence_matches": "overlapping",
    "sequence_texts": "distinct_inscriptions",
    "denominator": "nonzero_tokens",
    "zero_tokens": "excluded",
}

# Invented sign ids; not real inscriptions.
CORPUS = {
    "sign_list": "SYNTH",
    "inscriptions": [
        {"id": "T1", "signs": ["S1", "S2", "S3"]},
        {"id": "T2", "signs": ["S2", "S3", "S0"]},
    ],
}
COUNTS = {"S1": 1, "S2": 2, "S3": 2, "denominator": 5}


class ManifestTest(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self._write("source.txt", b"synthetic source A\n")
        self._write("corpus.json", json.dumps(CORPUS, indent=2).encode("utf-8"))
        self._write("count.py", b"def count(c):\n    return {}\n")
        self._write("counts.json", json.dumps(COUNTS).encode("utf-8"))
        self.manifest = m.build_manifest(["source.txt"], "corpus.json",
                                         ["count.py"], "counts.json",
                                         SEMANTICS, self.dir)
        self.manifest_path = os.path.join(self.dir, "manifest.json")
        with open(self.manifest_path, "w", encoding="utf-8") as f:
            json.dump(self.manifest, f)

    def tearDown(self):
        shutil.rmtree(self.dir)

    def _write(self, name, data):
        with open(os.path.join(self.dir, name), "wb") as f:
            f.write(data)

    def _flip_byte(self, name, old, new):
        path = os.path.join(self.dir, name)
        with open(path, "rb") as f:
            data = f.read()
        self.assertIn(old, data)
        self._write(name, data.replace(old, new, 1))

    def _check(self):
        return m.check_manifest(self.manifest, self.dir)

    def test_matching_manifest_passes(self):
        self.assertEqual(self._check(), [])
        self.assertEqual(m.check_manifest_file(self.manifest_path), [])

    def test_changed_source_byte_fails(self):
        self._flip_byte("source.txt", b"A", b"B")
        problems = self._check()
        self.assertEqual(len(problems), 1)
        self.assertIn("source_sha256", problems[0])

    def test_changed_corpus_byte_fails(self):
        self._flip_byte("corpus.json", b"S1", b"S9")
        problems = self._check()
        self.assertEqual(len(problems), 1)
        self.assertIn("corpus_sha256", problems[0])

    def test_corpus_hash_ignores_whitespace(self):
        self._write("corpus.json", json.dumps(CORPUS).encode("utf-8"))
        self.assertEqual(self._check(), [])

    def test_changed_code_byte_fails(self):
        self._flip_byte("count.py", b"{}", b"[]")
        problems = self._check()
        self.assertEqual(len(problems), 1)
        self.assertIn("code_sha256", problems[0])

    def test_changed_counts_fails(self):
        self._write("counts.json", json.dumps(dict(COUNTS, S1=9)).encode("utf-8"))
        problems = self._check()
        self.assertEqual(len(problems), 1)
        self.assertIn("counts_sha256", problems[0])

    def test_each_mismatch_reported_separately(self):
        self._flip_byte("source.txt", b"A", b"B")
        self._flip_byte("count.py", b"{}", b"[]")
        problems = self._check()
        self.assertEqual(len(problems), 2)
        self.assertTrue(any("source_sha256" in p for p in problems))
        self.assertTrue(any("code_sha256" in p for p in problems))

    def test_missing_field_fails(self):
        for field in m.REQUIRED_FIELDS:
            broken = dict(self.manifest)
            del broken[field]
            problems = m.check_manifest(broken, self.dir)
            self.assertEqual(problems, ["missing field: %s" % field])

    def test_unsupported_semantics_value_fails(self):
        self.manifest["semantics"] = dict(SEMANTICS, sequence_matches="sometimes")
        problems = self._check()
        self.assertEqual(len(problems), 1)
        self.assertIn("unsupported value", problems[0])

    def test_unsupported_semantics_key_fails(self):
        self.manifest["semantics"] = dict(SEMANTICS, rounding="up")
        problems = self._check()
        self.assertEqual(len(problems), 1)
        self.assertIn("unsupported key", problems[0])

    def test_contradictory_semantics_fails(self):
        self.manifest["semantics"] = dict(SEMANTICS, zero_tokens="included")
        problems = self._check()
        self.assertEqual(len(problems), 1)
        self.assertIn("contradictory", problems[0])

    def test_missing_semantics_key_fails(self):
        semantics = dict(SEMANTICS)
        del semantics["denominator"]
        self.manifest["semantics"] = semantics
        problems = self._check()
        self.assertEqual(problems, ["semantics: missing key 'denominator'"])

    def test_repeated_checks_identical(self):
        self._flip_byte("source.txt", b"A", b"B")
        self.assertEqual(self._check(), self._check())
        self.assertEqual(m.compute_hashes(self.manifest, self.dir),
                         m.compute_hashes(self.manifest, self.dir))

    def test_cli_exit_codes(self):
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(m.main(["check", self.manifest_path]), 0)
        self._flip_byte("count.py", b"{}", b"[]")
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(m.main(["check", self.manifest_path]), 1)
        self.assertIn("code_sha256", out.getvalue())

    def test_cli_build_then_check(self):
        out_path = os.path.join(self.dir, "built.json")
        args = ["build", "--source", os.path.join(self.dir, "source.txt"),
                "--corpus", os.path.join(self.dir, "corpus.json"),
                "--code", os.path.join(self.dir, "count.py"),
                "--counts", os.path.join(self.dir, "counts.json"),
                "--out", out_path]
        for k, v in sorted(SEMANTICS.items()):
            args += ["--semantics", "%s=%s" % (k, v)]
        with redirect_stdout(io.StringIO()):
            self.assertEqual(m.main(args), 0)
            self.assertEqual(m.main(["check", out_path]), 0)


if __name__ == "__main__":
    unittest.main()
