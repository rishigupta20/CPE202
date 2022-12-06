import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([5, 4, 6]), 6)
        self.assertEqual(max_list_iter([6, 4, 6]), 6)
        self.assertEqual(max_list_iter([6, 6, 6]), 6)
        self.assertEqual(max_list_iter([0, 8]), 8)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([0]), 0)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([3, 2, 3]), [3, 2, 3])
        self.assertEqual(reverse_rec([3]), [3])
        self.assertEqual(reverse_rec([0, 0]), [0, 0])
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([]), None)

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, 9, list_val), 4)
        list_val1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(5, 1, 2, list_val1)
        list_val2 = [1, 2, 3, 4]
        self.assertEqual(bin_search(3, 3, 1, list_val2), None)
        list_val3 = []
        self.assertEqual(bin_search(3, 1, 3, list_val3), None)
        list_val4 = [5]
        self.assertEqual(bin_search(5, 0, 1, list_val4), 0)
        list_val5 = [6]
        self.assertEqual(bin_search(5, 0, 1, list_val5), None)
        list_val6 = [1, 2, 3, 6, 10, 15, 90, 300, 1000]
        self.assertEqual(bin_search(90, 4, len(list_val6) - 1, list_val6), 6)
        self.assertEqual(bin_search(2, 0, len(list_val6) - 1, list_val6), 1)
        self.assertEqual(bin_search(1000, 0, len(list_val6) - 1, list_val6), 8)

    def test_reverse_mutate(self):
        list_val1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(list_val1)
        self.assertEqual(reverse_list_mutate([1, 2, 3]), None)
        self.assertEqual(reverse_list_mutate([]), None)
        self.assertEqual(reverse_list_mutate([12]), [12])


if __name__ == "__main__":
    unittest.main()
