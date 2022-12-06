class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        self.num_items += 1
        self.items[self.num_items] = item
        self.perc_up(self.num_items)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.items[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():
            return None
        temp = self.items[1]
        self.items[1], self.items[self.num_items] = self.items[self.num_items], None
        self.num_items -= 1
        self.perc_down(1)
        return temp

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        contents = []
        for val in self.items:
            if val is not None:
                contents.append(val)
        return contents

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        if self.capacity < len(alist):
            self.capacity = len(alist)
        self.items = [None] * (self.capacity + 1)
        self.num_items = len(alist)
        for idx in range(len(alist)):
            self.items[idx + 1] = alist[idx]
        i = self.num_items // 2
        while i > 0:
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        if self.num_items == self.capacity:
            return True
        return False

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.num_items

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i <= self.num_items // 2:
            if (i * 2) + 1 <= self.num_items and self.items[(i * 2) + 1] > self.items[i * 2] and \
                    self.items[(i * 2) + 1] > self.items[i]:
                temp = self.items[(i * 2) + 1]
                self.items[(i * 2) + 1] = self.items[i]
                self.items[i] = temp
                i = (i * 2) + 1
            elif i * 2 <= self.num_items and self.items[i * 2] > self.items[i]:
                temp = self.items[i * 2]
                self.items[i * 2] = self.items[i]
                self.items[i] = temp
                i = i * 2
            else:
                break

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 > 0:
            if self.items[i] > self.items[i // 2]:
                temp = self.items[i // 2]
                self.items[i // 2] = self.items[i]
                self.items[i] = temp
            i = i // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        for idx in range(len(alist) - 1, -1, -1):
            alist[idx] = self.dequeue()
