import unittest
from hash_quad import *


class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0)  # Causes rehash
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

    def test_03(self):
        ht = HashTable(121)
        ht.insert("a", 0)
        ht.insert("a", 0)

    def test_04(self):
        ht = HashTable(2)

    def test_05(self):
        ht = HashTable(0)

    def test_06(self):
        ht = HashTable(121)

    def test_07(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0)  # Causes rehash
        self.assertTrue(ht.in_table("a"))
        self.assertTrue(ht.in_table("h"))
        self.assertTrue(ht.in_table("o"))
        self.assertTrue(ht.in_table("v"))
        self.assertFalse(ht.in_table("z"))

    def test_08(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("z"), None)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0)  # Causes rehash

    def test_09(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0)  # Causes rehash
        self.assertEqual(ht.get_value("a"), 0)
        self.assertEqual(ht.get_value("h"), 0)
        self.assertEqual(ht.get_value("o"), 0)
        self.assertEqual(ht.get_value("v"), 0)
        self.assertEqual(ht.get_value("p"), None)

    def test_10(self):
        ht = HashTable(2)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 1)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 4)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 1)
        ht.insert("v", 0)  # Causes rehash
        self.assertEqual(ht.get_value("a"), 0)
        self.assertEqual(ht.get_value("h"), 0)
        self.assertEqual(ht.get_value("o"), 0)
        self.assertEqual(ht.get_value("v"), 0)
        self.assertEqual(ht.get_value("p"), None)

    def test_11(self):
        ht = HashTable(3)
        ht.insert("a", 0)
        self.assertTrue(ht.in_table("a"), 1)
        ht.insert("d", 0)
        self.assertFalse(ht.in_table("h"), 3)

    def test_12(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_value("a"), 0)
        ht.insert("f", 0)
        self.assertEqual(ht.get_value("f"), 0)

    def test_13(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_value("a"), 0)
        ht.insert("h", 0)
        self.assertEqual(ht.get_value("h"), 0)


if __name__ == '__main__':
    unittest.main()
