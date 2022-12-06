import unittest
from base_convert import *


class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45, 2), "101101")
        self.assertEqual(convert(0, 2), "0")
        self.assertEqual(convert(1, 2), "1")
        self.assertEqual(convert(1456, 2), "10110110000")

    def test_base3(self):
        self.assertEqual(convert(1900, 3), "2121101")

    def test_base4(self):
        self.assertEqual(convert(30, 4), "132")
        self.assertEqual(convert(0, 4), "0")
        self.assertEqual(convert(1, 4), "1")

    def test_base8(self):
        self.assertEqual(convert(1999, 8), "3717")

    def test_base10(self):
        self.assertEqual(convert(1994, 10), "1994")

    def test_base12(self):
        self.assertEqual(convert(0, 12), "0")

    def test_base13(self):
        self.assertEqual(convert(1959, 13), "B79")

    def test_base15(self):
        self.assertEqual(convert(1995, 15), "8D0")

    def test_base16(self):
        self.assertEqual(convert(316, 16), "13C")
        self.assertEqual(convert(1959, 16), "7A7")
        self.assertEqual(convert(1999, 16), "7CF")
        self.assertEqual(convert(199999999, 16), "BEBC1FF")
        self.assertEqual(convert(19892, 16), "4DB4")


if __name__ == "__main__":
    unittest.main()
