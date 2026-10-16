import json
import os
import tempfile
import unittest

from indus.corpus import load_corpus

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "tiny_corpus.json")


def good():
    return {"source": "s", "license": "l", "sign_list": "SYNTH",
            "inscriptions": [{"id": "a", "site": None, "signs": ["S1"]}]}


class CorpusTest(unittest.TestCase):
    def load(self, data):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "c.json")
            with open(p, "w") as f:
                json.dump(data, f)
            return load_corpus(p)

    def test_valid(self):
        c = load_corpus(FIX)
        self.assertEqual(len(c.inscriptions), 8)
        self.assertEqual(c.sign_list, "SYNTH")
        self.assertEqual(c.source, "synthetic test fixture")
        self.assertEqual(c.license, "CC0")
        self.assertEqual(c.inscriptions[0].signs[:2], ["S1", "S2"])

    def test_missing_top_level(self):
        for k in ("source", "license", "sign_list", "inscriptions"):
            d = good()
            del d[k]
            with self.assertRaisesRegex(ValueError, k):
                self.load(d)

    def test_missing_inscription_field(self):
        for k in ("id", "site", "signs"):
            d = good()
            del d["inscriptions"][0][k]
            with self.assertRaisesRegex(ValueError, k):
                self.load(d)

    def test_duplicate_ids(self):
        d = good()
        d["inscriptions"].append(dict(d["inscriptions"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.load(d)

    def test_empty_signs(self):
        d = good()
        d["inscriptions"][0]["signs"] = []
        with self.assertRaisesRegex(ValueError, "empty"):
            self.load(d)


if __name__ == "__main__":
    unittest.main()
