import unittest
from bears import *


# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_05(self):
        self.assertFalse(bears(240))

    def test_bear_06(self):
        self.assertFalse(bears(10001))

    def test_bear_07(self):
        self.assertTrue(bears(288))

    def test_bear_08(self):
        self.assertFalse(bears(120))

    def test_bear_09(self):
        self.assertTrue(bears(168))

    def test_bear_10(self):
        self.assertFalse(bears(133))

    def test_bear_11(self):
        self.assertFalse(bears(1))


if __name__ == "__main__":
    unittest.main()
