import unittest

from indus.sequence import count_sequence

# Synthetic fixtures only: invented integer sign ids, not corpus rows.


class CountSequenceTest(unittest.TestCase):
    def check(self, inscriptions, sequence, matches, texts):
        self.assertEqual(count_sequence(inscriptions, sequence),
                         {"matches": matches, "texts": texts})

    def test_no_match(self):
        self.check([[1, 2, 3], [4, 5]], [3, 1], 0, 0)

    def test_one_match(self):
        self.check([[1, 2, 3], [4, 5]], [2, 3], 1, 1)

    def test_overlapping_match(self):
        # 5,5 starts at positions 0 and 1 of 5,5,5
        self.check([[5, 5, 5]], [5, 5], 2, 1)

    def test_match_at_first_position(self):
        self.check([[7, 8, 9, 10]], [7, 8], 1, 1)

    def test_match_at_last_position(self):
        self.check([[7, 8, 9, 10]], [9, 10], 1, 1)

    def test_sequence_longer_than_inscription(self):
        self.check([[1, 2]], [1, 2, 3], 0, 0)

    def test_one_token_inscription(self):
        self.check([[4]], [4], 1, 1)
        self.check([[4]], [4, 4], 0, 0)

    def test_empty_list_of_inscriptions(self):
        self.check([], [1, 2], 0, 0)

    def test_same_sequence_in_two_inscriptions(self):
        self.check([[1, 2, 3], [9, 1, 2], [3, 3]], [1, 2], 2, 2)

    def test_sequence_of_length_three(self):
        self.check([[1, 2, 3, 1, 2, 3], [2, 3, 1], [1, 2, 4]], [1, 2, 3], 2, 1)

    def test_repeats_in_one_inscription_count_one_text(self):
        # three non-overlapping matches in one text, one in another
        self.check([[6, 7, 6, 7, 6, 7], [6, 7]], [6, 7], 4, 2)

    def test_empty_sequence_rejected(self):
        with self.assertRaises(ValueError):
            count_sequence([[1, 2]], [])


if __name__ == "__main__":
    unittest.main()
