import unittest

from indus.frequency import sign_frequency_claim, token_totals

# Synthetic fixtures only: invented integer sign ids, not corpus rows.
# 10 tokens, 3 of them sign 0, one uncertain token of sign 4.
MIXED = [[1, 2, 0], [1, 1, 3], [0, 0], [(4, True), 1]]
ONLY_ZERO = [[0], [0, 0]]
EMPTY = []


class FrequencyContractTest(unittest.TestCase):
    def test_zero_tokens_excluded_from_denominator(self):
        self.assertEqual(token_totals(MIXED)["nonzero_tokens"], 7)
        self.assertEqual(sign_frequency_claim(MIXED, 1)["denominator_value"], 7)

    def test_totals_add_up(self):
        for fixture in (MIXED, ONLY_ZERO, EMPTY):
            t = token_totals(fixture)
            self.assertEqual(t["all_tokens"],
                             t["nonzero_tokens"] + t["excluded_zero_tokens"])
        self.assertEqual(token_totals(MIXED)["all_tokens"], 10)
        self.assertEqual(token_totals(MIXED)["excluded_zero_tokens"], 3)

    def test_tokens_alias_is_nonzero_tokens(self):
        t = token_totals(MIXED)
        self.assertEqual(t["tokens"], t["nonzero_tokens"])
        self.assertNotEqual(t["tokens"], t["all_tokens"])

    def test_percent_uses_nonzero_not_all_tokens(self):
        # sign 1: 4 of 7 nonzero tokens = 57.14; over all 10 it would be 40.0
        self.assertEqual(sign_frequency_claim(MIXED, 1)["percent"], 57.14)

    def test_percent_rounding_rule(self):
        # 1 of 7: round(1428.57...) / 100
        self.assertEqual(sign_frequency_claim(MIXED, 2)["percent"], 14.29)

    def test_sign_zero_gets_no_percent(self):
        with self.assertRaises(ValueError):
            sign_frequency_claim(MIXED, 0)

    def test_uncertain_nonzero_token_counts(self):
        claim = sign_frequency_claim(MIXED, 4)
        self.assertEqual((claim["occurrences"], claim["texts"]), (1, 1))
        self.assertEqual(claim["percent"], 14.29)

    def test_same_sign_twice_in_one_inscription_is_one_text(self):
        claim = sign_frequency_claim(MIXED, 1)
        self.assertEqual(claim["occurrences"], 4)
        self.assertEqual(claim["texts"], 3)

    def test_occurrences_of_all_signs_sum_to_nonzero_tokens(self):
        nonzero = token_totals(MIXED)["nonzero_tokens"]
        claims = [sign_frequency_claim(MIXED, s) for s in (1, 2, 3, 4)]
        self.assertEqual(sum(c["occurrences"] for c in claims), nonzero)
        for c in claims:
            self.assertEqual(c["denominator_value"], nonzero)
            self.assertEqual(c["percent"],
                             round(10000 * c["occurrences"] / nonzero) / 100)
        # rounding can move each percent by at most 0.005
        self.assertAlmostEqual(sum(c["percent"] for c in claims), 100.0,
                               delta=0.005 * len(claims))

    def test_only_zero_tokens_no_division_by_zero(self):
        t = token_totals(ONLY_ZERO)
        self.assertEqual((t["all_tokens"], t["nonzero_tokens"],
                          t["excluded_zero_tokens"]), (3, 0, 3))
        claim = sign_frequency_claim(ONLY_ZERO, 1)
        self.assertEqual((claim["occurrences"], claim["texts"]), (0, 0))
        self.assertIsNone(claim["percent"])

    def test_empty_fixture_no_division_by_zero(self):
        self.assertEqual(token_totals(EMPTY),
                         {"all_tokens": 0, "nonzero_tokens": 0,
                          "excluded_zero_tokens": 0, "tokens": 0})
        self.assertIsNone(sign_frequency_claim(EMPTY, 1)["percent"])


if __name__ == "__main__":
    unittest.main()
