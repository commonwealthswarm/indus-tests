import os
import unittest

from indus.corpus import Corpus, Inscription, load_corpus
from indus.readings import Reading, load_reading
from indus.score import render, score

FIX = os.path.join(os.path.dirname(__file__), "fixtures")


def corpus(*texts):
    return Corpus("synthetic", "CC0", "SYNTH",
                  [Inscription("T%d" % i, None, list(t)) for i, t in enumerate(texts)])


def reading(values, lexicon=()):
    return Reading("r", "a", 2026, "c", "SYNTH", "synthetic", dict(values), list(lexicon))


class FixtureScoreTest(unittest.TestCase):
    def setUp(self):
        self.corpus = load_corpus(os.path.join(FIX, "tiny_corpus.json"))
        self.reading = load_reading(os.path.join(FIX, "tiny_reading.json"))

    def test_metrics(self):
        m = score(self.corpus, self.reading)
        self.assertEqual(set(m), {"coverage_tokens", "coverage_types", "full_inscriptions",
                                  "consistency", "repeat_agreement", "lexicon_hits"})
        # 26 tokens (5+3+4+4+2+3+2+3); unmapped: S7 x2, S8 x2, S9 x2, S10 x1 = 7
        self.assertAlmostEqual(m["coverage_tokens"], 19 / 26)
        # 10 distinct signs S1..S10, 6 mapped (S1..S6)
        self.assertAlmostEqual(m["coverage_types"], 0.6)
        # only T1 and T2 are fully mapped, of 8
        self.assertAlmostEqual(m["full_inscriptions"], 0.25)
        # S1..S6 all occur and all have one string value: 6/6
        self.assertAlmostEqual(m["consistency"], 1.0)
        # n-grams in >= 2 inscriptions: S1S2 (T1,T2,T3), S3S4 (T1,T4),
        # S4S5 (T1,T4), S3S4S5 (T1,T4); no 4-gram repeats; all single-valued: 4/4
        self.assertAlmostEqual(m["repeat_agreement"], 1.0)
        # ka-ma = S1S2 in T1, T2, T3 (3); ta-ri-nu = S3S4S5 in T1, T4 (2)
        self.assertEqual(m["lexicon_hits"], 5)
        self.assertIsInstance(m["lexicon_hits"], int)

    def test_empty_lexicon(self):
        r = reading(self.reading.values)
        self.assertEqual(score(self.corpus, r)["lexicon_hits"], 0)


class RenderTest(unittest.TestCase):
    def test_unmapped_sign(self):
        r = load_reading(os.path.join(FIX, "tiny_reading.json"))
        self.assertEqual(render(r, ["S1", "S7", "S2"]), "ka-?-ma")

    def test_multi_valued_uses_first(self):
        r = reading({"S1": ["a", "b"], "S2": ["c"], "S3": "d"})
        self.assertEqual(render(r, ["S1", "S2", "S3"]), "a-c-d")


class EdgeCaseScoreTest(unittest.TestCase):
    def test_empty_corpus(self):
        m = score(corpus(), reading({"S1": "a"}, ["a"]))
        self.assertEqual(m, {"coverage_tokens": 0.0, "coverage_types": 0.0,
                             "full_inscriptions": 0.0, "consistency": 0.0,
                             "repeat_agreement": 0.0, "lexicon_hits": 0})

    def test_repeat_within_one_inscription_ignored(self):
        # S1S1 occurs twice but only in T0; S1S1S1 once: no eligible n-gram
        m = score(corpus(["S1", "S1", "S1"], ["S2"]), reading({"S1": "a"}))
        self.assertEqual(m["repeat_agreement"], 0.0)
        # S1S1 now in two different inscriptions: 1/1
        m = score(corpus(["S1", "S1"], ["S1", "S1"]), reading({"S1": "a"}))
        self.assertEqual(m["repeat_agreement"], 1.0)

    def test_ambiguous_versus_one_element_list(self):
        c = corpus(["S1", "S2", "S3"], ["S1", "S2"])
        # S9 is mapped but absent from the corpus, so it is not counted
        r = reading({"S1": ["a", "b"], "S2": ["c"], "S9": ["x", "y"]})
        m = score(c, r)
        self.assertAlmostEqual(m["coverage_tokens"], 4 / 5)    # S3 unmapped
        self.assertAlmostEqual(m["coverage_types"], 2 / 3)     # S1, S2 of S1..S3
        self.assertAlmostEqual(m["full_inscriptions"], 0.5)    # only T1
        self.assertAlmostEqual(m["consistency"], 0.5)          # S2 single, S1 not
        self.assertAlmostEqual(m["repeat_agreement"], 0.0)     # S1S2 has ambiguous S1

    def test_unmapped_windows_never_match(self):
        # windows from S1,S2,S1 with no unmapped sign: S1 at 0 and S1 at 2;
        # the duplicate "a" entry does not double-count
        r = reading({"S1": "a"}, ["a", "a", "a-?", "?", "?-a"])
        self.assertEqual(score(corpus(["S1", "S2", "S1"]), r)["lexicon_hits"], 2)

    def test_multi_valued_lexicon_uses_first_value(self):
        c = corpus(["S1"])
        self.assertEqual(score(c, reading({"S1": ["a", "b"]}, ["a"]))["lexicon_hits"], 1)
        self.assertEqual(score(c, reading({"S1": ["a", "b"]}, ["b"]))["lexicon_hits"], 0)

    def test_length_six_cutoff(self):
        # seven S1: two windows of length 6 match; length 7 is never tried
        r = reading({"S1": "a"}, ["-".join(["a"] * 6), "-".join(["a"] * 7)])
        self.assertEqual(score(corpus(["S1"] * 7), r)["lexicon_hits"], 2)


if __name__ == "__main__":
    unittest.main()
