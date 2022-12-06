import unittest
from binary_search_tree import *


class TestLab5(unittest.TestCase):

    def test_simple1(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_simple2(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.search(15))

    def test_simple3(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertFalse(bst.is_empty())
        self.assertFalse(bst.search(15))
        self.assertTrue(bst.search(10))
        bst.insert(20, 'p')
        bst.insert(40, 'l')
        bst.insert(70, 'z')
        bst.insert(2, 'm')
        bst.insert(5, 'po')
        self.assertFalse(bst.search(15))
        self.assertTrue(bst.search(70))
        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(40))
        self.assertFalse(bst.search(99))

    def test_simple4(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_min(), None)
        self.assertNotEqual(bst.find_min(), 15)

    def test_simple5(self):
        bst = BinarySearchTree()
        bst.insert(50, '90')
        bst.insert(9, '90')
        bst.insert(49, 'po')
        bst.insert(60, 'hi')
        bst.insert(55, 'jo')
        bst.insert(55, 'poo')
        bst.insert(51, 'loo')
        self.assertEqual(bst.find_min(), (9, '90'))
        bst.insert(9, 14)
        self.assertEqual(bst.find_min(), (9, 14))
        bst.insert(9, None)
        self.assertEqual(bst.find_min(), (9, None))

    def test_simple6(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_max(), None)
        self.assertNotEqual(bst.find_max(), 'poo')
        self.assertNotEqual(bst.find_max(), 14)
        bst.insert(50, '90')
        bst.insert(9, '90')
        bst.insert(49, 'po')
        bst.insert(60, 'hi')
        bst.insert(55, 'jo')
        bst.insert(55, 'poo')
        bst.insert(51, 'loo')
        self.assertEqual(bst.find_max(), (60, 'hi'))
        self.assertNotEqual(bst.find_max(), (None, None))

    def test_simple7(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.assertNotEqual(bst.tree_height(), 'five')
        bst.insert(50, '90')
        bst.insert(9, '90')
        bst.insert(49, 'po')
        bst.insert(60, 'hi')
        bst.insert(55, 'jo')
        bst.insert(55, 'poo')
        bst.insert(51, 'loo')
        bst.insert(44, 'zoo')
        bst.insert(7, 'looo')
        self.assertEqual(bst.tree_height(), 3)
        bst.insert(47, 'loo')
        self.assertEqual(bst.tree_height(), 4)

    def test_simple8(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), [])
        bst.insert(50, '90')
        bst.insert(9, '90')
        bst.insert(49, 'po')
        bst.insert(60, 'hi')
        bst.insert(55, 'jo')
        bst.insert(55, 'poo')
        bst.insert(51, 'loo')
        bst.insert(44, 'zoo')
        bst.insert(7, 'looo')
        bst.insert(47, 'l')
        self.assertEqual(bst.inorder_list(), [7, 9, 44, 47, 49, 50, 51, 55, 60])

    def test_simple9(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        bst.insert(50, '90')
        bst.insert(9, '90')
        bst.insert(49, 'po')
        bst.insert(60, 'hi')
        bst.insert(55, 'jo')
        bst.insert(55, 'poo')
        bst.insert(51, 'loo')
        bst.insert(44, 'zoo')
        bst.insert(7, 'looo')
        bst.insert(47, 'l')
        bst.insert(47, 'p')
        self.assertEqual(bst.preorder_list(), [50, 9, 7, 49, 44, 47, 60, 55, 51])

    def test_simple10(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.level_order_list(), [])
        bst.insert(50, '90')
        bst.insert(9, '90')
        bst.insert(49, 'po')
        bst.insert(60, 'hi')
        bst.insert(55, 'jo')
        bst.insert(55, 'poo')
        bst.insert(51, 'loo')
        bst.insert(44, 'zoo')
        bst.insert(7, 'looo')
        bst.insert(47, 'l')
        self.assertEqual(bst.level_order_list(), [50, 9, 60, 7, 49, 55, 44, 51, 47])


if __name__ == '__main__':
    unittest.main()
