class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None
        self.num_items = 0
        self.back = None

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full() is True:
            raise IndexError
        n = Node(item)
        self.num_items += 1
        if self.num_items == 1:
            self.back = n
            self.front = n

        if self.num_items > 1:
            self.back.next = n
            self.back = n

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty() is True:
            raise IndexError
        temp = self.front.data
        self.front = self.front.next
        self.num_items -= 1
        return temp

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
