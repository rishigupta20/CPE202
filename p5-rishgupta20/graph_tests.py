import unittest
from graph import *


class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertex('v5'), None)
        self.assertEqual(g.get_vertex('v1').id, 'v1')

    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h']])
        self.assertTrue(g.is_bipartite())

    def test_04(self):
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8']])
        self.assertTrue(g.is_bipartite())

    def test_05(self):
        g = Graph('test5.txt')
        self.assertEqual(g.conn_components(), [['CH', 'NJ', 'NY'], ['LA', 'SD', 'SF', 'SJ']])
        self.assertTrue(g.is_bipartite())

    def test_06(self):
        g = Graph('test6.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5']])
        self.assertFalse(g.is_bipartite())

    def test_07(self):
        g = Graph('test7.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7'])


if __name__ == '__main__':
    unittest.main()
