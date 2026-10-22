import os
import time
import unittest

from indus.baseline import null_baseline
from indus.corpus import load_corpus
from indus.readings import load_reading

FIX = os.path.join(os.path.dirname(__file__), "fixtures")


class BaselineTest(unittest.TestCase):
    def setUp(self):
        self.corpus = load_corpus(os.path.join(FIX, "tiny_corpus.json"))
        self.reading = load_reading(os.path.join(FIX, "tiny_reading.json"))

    def test_same_seed_identical(self):
        a = null_baseline(self.corpus, self.reading, n=50, seed=7)
        b = null_baseline(self.corpus, self.reading, n=50, seed=7)
        self.assertEqual(a, b)
        self.assertEqual(set(a), {"observed", "null_mean", "null_sd", "p_value", "n"})

    def test_tiny_fixture_beats_shuffle(self):
        # observed = 5 (ka-ma x3 at S1S2, ta-ri-nu x2 at S3S4S5); 5 is the
        # maximum and only the identity permutation (1 of 720) reaches it.
        start = time.perf_counter()
        r = null_baseline(self.corpus, self.reading, n=200)
        self.assertLess(time.perf_counter() - start, 5.0)
        self.assertEqual(r["observed"], 5)
        self.assertEqual(r["n"], 200)
        self.assertLess(r["p_value"], 0.5)
        self.assertLess(r["null_mean"], 5)

    def test_invariant_metric_has_zero_spread(self):
        r = null_baseline(self.corpus, self.reading, metric="coverage_tokens", n=20)
        self.assertAlmostEqual(r["null_mean"], 19 / 26)
        self.assertAlmostEqual(r["null_sd"], 0.0)
        self.assertAlmostEqual(r["p_value"], 1.0)

    def test_bad_arguments(self):
        with self.assertRaises(ValueError):
            null_baseline(self.corpus, self.reading, n=0)
        with self.assertRaises(ValueError):
            null_baseline(self.corpus, self.reading, metric="nope", n=10)


if __name__ == "__main__":
    unittest.main()
