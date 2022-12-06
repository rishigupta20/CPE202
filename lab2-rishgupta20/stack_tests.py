import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# from stack_array import Stack

from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        stack.push(0)
        stack.push(2)
        self.assertFalse(stack.is_empty())
        stack.push(None)
        stack.push('Five')
        stack.push(4)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 5)
        val = stack.pop()
        self.assertEqual(val, 4)
        self.assertNotEqual(val, 5)

    def test_simple1(self):
        stack = Stack(3)
        stack.push(4)
        stack.push('Five')
        stack.push('Fire')
        stack.pop()
        stack.push('Fire')

        with self.assertRaises(IndexError):
            stack.push(2)

    def test_simple2(self):
        stack = Stack(1)
        stack.push(2)
        stack.pop()

        with self.assertRaises(IndexError):
            stack.pop()

    def test_simple3(self):
        stack = Stack(3)
        stack.push(2)
        stack.push(3)
        stack.push(5)
        with self.assertRaises(IndexError):
            stack.push(2)

    def test_simple4(self):
        stack = Stack(1)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_simple5(self):
        stack = Stack(2)
        stack.push(None)
        stack.push(None)
        stack.pop()
        stack.pop()

        with self.assertRaises(IndexError):
            stack.peek()

    def test_simple6(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertTrue(stack.is_full())
        stack.pop()
        self.assertFalse(stack.is_full())

    def test_simple7(self):
        stack = Stack(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)

    def test_simple8(self):
        stack = Stack(3)
        stack.push(2)
        stack.push(4)
        self.assertEqual(4, stack.pop())

    def test_simple9(self):
        stack = Stack(2)
        stack.push(4)
        self.assertEqual(stack.peek(), 4)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_simple10(self):
        stack = Stack(4)
        stack.push(2)
        self.assertEqual(1, stack.size())

    def test_simple11(self):
        stack = Stack(2)
        stack.push(4)
        stack.push('five')
        with self.assertRaises(IndexError):
            stack.push(4)

    def test_simple12(self):
        stack = Stack(0)
        with self.assertRaises(IndexError):
            stack.push(4)

    def test_simple13(self):
        stack = Stack(4)
        stack.push(None)
        self.assertEqual(stack.peek(), None)
        stack.push('Four')
        stack.push(None)
        stack.push('3')
        with self.assertRaises(IndexError):
            stack.push(None)

    def test_simple14(self):
        stack = Stack(2)
        stack.push(3)
        stack.pop()

        with self.assertRaises(IndexError):
            stack.peek()

    def test_simple15(self):
        stack = Stack(2)
        self.assertEqual(stack.size(), 0)
        self.assertNotEqual(stack.size(), 2)



if __name__ == '__main__':
    unittest.main()
