import unittest
from sorts import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_simple1(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_simple2(self):
        nums = []
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

    def test_simple3(self):
        nums = []
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

    def test_simple4(self):
        nums = [4]
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [4])

    def test_simple5(self):
        nums = [4]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [4])

    def test_simple6(self):
        nums = [23, 10, 99, 101, 85]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [10, 23, 85, 99, 101])

    def test_simple7(self):
        nums = [23, 10, 99, 101, 85]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [10, 23, 85, 99, 101])

    def test_simple8(self):
        nums = [23, 10, 99, 101, 85]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [10, 23, 85, 99, 101])

    def test_simple9(self):
        nums = [23, 10, 99, 101, 85]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [10, 23, 85, 99, 101])

    def test_simple10(self):
        nums = [5, 7, 9, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 3)
        self.assertEqual(nums, [5, 7, 9, 10])

    def test_simple11(self):
        nums = [5, 7, 9, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [5, 7, 9, 10])


if __name__ == '__main__':
    unittest.main()
