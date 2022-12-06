class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = 0
        self.back = 0

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
        if self.is_full():
            raise IndexError
        if self.is_empty():
            self.items[self.front] = item
            self.num_items += 1
            self.back += 1
            return

        if self.back == self.capacity - 1:
            self.items[self.back] = item
            self.num_items += 1
            self.back = 0
            return

        self.items[self.back] = item
        self.num_items += 1
        self.back += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty() is True:
            raise IndexError

        if self.front == self.capacity - 1:
            temp = self.items[self.front]
            self.items[self.front] = None
            self.front = 0
            self.num_items -= 1
            return temp

        temp = self.items[self.front]
        self.items[self.front] = None
        self.num_items -= 1
        self.front += 1
        return temp

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
