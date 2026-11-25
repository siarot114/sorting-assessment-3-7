import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import FULL_NAME, build_unsorted_array, insertion_sort


class TestSorting(unittest.TestCase):
    def test_no_duplicates_or_symbols(self):
        arr = build_unsorted_array(FULL_NAME)
        self.assertEqual(len(arr), len(set(arr)))
        self.assertTrue(all(c.isalpha() for c in arr))

    def test_sorted_result(self):
        arr = build_unsorted_array(FULL_NAME)
        self.assertEqual(insertion_sort(arr), sorted(arr))


if __name__ == "__main__":
    unittest.main()
