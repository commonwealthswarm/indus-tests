import json
import os
import tempfile
import unittest

from indus.readings import load_reading, load_readings

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "tiny_reading.json")


def good():
    return {"name": "n", "author": "a", "year": 1990, "citation": "c",
            "sign_list": "SYNTH", "language": "l", "values": {"S1": "ka"}}


class ReadingsTest(unittest.TestCase):
    def load(self, data, name="r.json"):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, name)
            with open(p, "w") as f:
                json.dump(data, f)
            return load_reading(p)

    def test_fixture(self):
        r = load_reading(FIX)
        self.assertEqual(r.sign_list, "SYNTH")
        self.assertEqual(sorted(r.values), ["S1", "S2", "S3", "S4", "S5", "S6"])
        self.assertEqual(len(set(r.values.values())), 6)
        self.assertEqual(r.lexicon, ["ka-ma", "ta-ri-nu"])

    def test_defaults(self):
        r = self.load(good())
        self.assertEqual(r.lexicon, [])
        self.assertEqual(r.notes, "")
        self.assertEqual(r.year, 1990)

    def test_list_values(self):
        d = good()
        d["values"] = {"S1": ["ka", "ga"], "S2": ["ma"]}
        r = self.load(d)
        self.assertEqual(r.values["S1"], ["ka", "ga"])

    def test_missing_required(self):
        for k in ("name", "author", "year", "citation", "sign_list", "language", "values"):
            d = good()
            del d[k]
            with self.assertRaisesRegex(ValueError, "r.json.*" + k):
                self.load(d)

    def test_empty_values(self):
        d = good()
        d["values"] = {}
        with self.assertRaisesRegex(ValueError, "r.json.*empty values"):
            self.load(d)

    def test_bad_value(self):
        for bad in ("", [], [""], ["ka", ""], 3, None, ["ka", 1]):
            d = good()
            d["values"] = {"S1": bad}
            with self.assertRaisesRegex(ValueError, "r.json.*S1"):
                self.load(d)

    def test_year_not_int(self):
        for bad in ("1990", 1990.0, True):
            d = good()
            d["year"] = bad
            with self.assertRaisesRegex(ValueError, "r.json.*year"):
                self.load(d)

    def test_sign_list_not_string(self):
        d = good()
        d["sign_list"] = 77
        with self.assertRaisesRegex(ValueError, "r.json.*sign_list"):
            self.load(d)

    def test_load_readings_sorted(self):
        with tempfile.TemporaryDirectory() as d:
            for n in ("b.json", "a.json"):
                x = good()
                x["name"] = n
                with open(os.path.join(d, n), "w") as f:
                    json.dump(x, f)
            self.assertEqual([r.name for r in load_readings(d)], ["a.json", "b.json"])


if __name__ == "__main__":
    unittest.main()
