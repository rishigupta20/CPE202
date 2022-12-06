import unittest
# from queue_array import Queue


from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue1(self):
        q = Queue(3)
        q.enqueue(4)
        q.enqueue(9)
        q.enqueue(4)
        q.dequeue()
        q.enqueue('five')
        self.assertTrue(q.is_full())
        q.dequeue()
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        q.dequeue()
        q.dequeue()
        self.assertTrue(q.is_empty())

        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue2(self):
        q = Queue(2)
        q.enqueue(1)
        q.enqueue(None)

        with self.assertRaises(IndexError):
            q.enqueue(2)

    def test_queue3(self):
        q = Queue(4)
        self.assertNotEqual(q.size(), 2)
        self.assertEqual(q.size(), 0)
        q.enqueue(4)
        q.enqueue(2)
        val = q.dequeue()
        val1 = q.dequeue()
        self.assertEqual(val, 4)
        self.assertEqual(val1, 2)

    def test_queue4(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        val = q.dequeue()
        self.assertEqual(val, 1)
        val1 = q.dequeue()
        self.assertEqual(val1, 2)
        val2 = q.dequeue()
        self.assertEqual(val2, 3)
        q.enqueue(None)
        q.enqueue('Four')
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 2)
        q.enqueue('5')
        self.assertTrue(q.is_full())


if __name__ == '__main__':
    unittest.main()
