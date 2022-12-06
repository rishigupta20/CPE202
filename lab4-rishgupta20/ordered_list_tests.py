import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_simple1(self):
        t_list = OrderedList()
        t_list.add(10)
        val1 = t_list.add(10)
        self.assertFalse(t_list.is_empty())
        self.assertFalse(val1)
        val2 = t_list.add(5)
        self.assertTrue(val2)
        val3 = t_list.add(20)
        self.assertTrue(val3)
        val3 = t_list.add(20)
        self.assertFalse(val3)

    def test_simple2(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        self.assertEqual(t_list.size(), 2)
        self.assertEqual(t_list.python_list(), [10, 20])

    def test_add_remove(self):
        t_list = OrderedList()
        t_list.remove(2)
        t_list.add(15)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.head.next.item, 15)
        self.assertEqual(t_list.head.prev.item, 30)
        t_list.add(5)
        self.assertEqual(t_list.head.next.item, 5)
        self.assertEqual(t_list.head.prev.item, 30)
        t_list.add(60)
        self.assertEqual(t_list.head.next.item, 5)
        self.assertEqual(t_list.head.prev.item, 60)
        t_list.add(45)
        self.assertListEqual(t_list.python_list(), [5, 15, 20, 30, 45, 60])
        t_list.remove(5)
        self.assertEqual(t_list.head.next.item, 15)
        self.assertEqual(t_list.head.prev.item, 60)
        t_list.remove(45)
        self.assertEqual(t_list.head.next.item, 15)
        self.assertEqual(t_list.head.prev.item, 60)
        t_list.remove(20)
        t_list.add(22)
        t_list.remove(20)
        self.assertEqual(t_list.python_list(), [15, 22, 30, 60])

    def test_index_pop(self):
        t_list = OrderedList()
        t_list.add(4)
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.index(4), 0)
        self.assertEqual(t_list.index(10), 1)
        self.assertEqual(t_list.index(25), None)
        z = t_list.pop(0)
        self.assertEqual(z, 4)
        x = t_list.pop(0)
        self.assertEqual(x, 10)
        t_list.add(5)
        t_list.add(10)
        x = t_list.pop(3)
        with self.assertRaises(IndexError):
            t_list.pop(-1)

    def test_search(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertTrue(t_list.search(5))
        self.assertTrue(t_list.search(30))
        self.assertFalse(t_list.search(33))
        self.assertFalse(t_list.search(0))


    def test_python_list(self):
        t_list = OrderedList()
        self.assertListEqual(t_list.python_list(), [])
        self.assertListEqual(t_list.python_list_reversed(), [])
        t_list.add(5)
        self.assertListEqual(t_list.python_list(), [5])
        self.assertListEqual(t_list.python_list_reversed(), [5])
        t_list.add(10)
        t_list.add(15)
        t_list.add(20)
        self.assertListEqual(t_list.python_list(), [5, 10, 15, 20])
        self.assertListEqual(t_list.python_list_reversed(), [20, 15, 10, 5])

    def test_size(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)
        t_list.add(5)
        t_list.add(10)
        t_list.add(15)
        t_list.add(20)
        self.assertEqual(t_list.size(), 4)
        t_list.remove(20)
        self.assertEqual(t_list.size(), 3)
        t_list.pop(0)
        self.assertEqual(t_list.size(), 2)

    def test_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(5)
        self.assertFalse(t_list.is_empty())

    def test_pop2(self):
        t_list = OrderedList()
        t_list.add(4)
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        with self.assertRaises(IndexError):
            t_list.pop(4)







if __name__ == '__main__':
    unittest.main()
