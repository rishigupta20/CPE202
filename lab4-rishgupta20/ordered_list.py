class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        dummy = Node('Dummy')
        dummy.next = dummy
        dummy.prev = dummy
        self.head = dummy

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head == self.head.prev:
            return True

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  Assume that all items added to your 
           list can be compared using the < operator and can be compared for equality/inequality.
           Make no other assumptions about the items in your list'''
        node1 = Node(item)
        node2 = self.head.next
        while node2 != self.head:
            if node2.item < node1.item:
                node2 = node2.next
            elif node2.item == node1.item:
                return False
            elif node2.item > node1.item:
                node2.prev.next = node1
                node1.prev = node2.prev
                node1.next = node2
                node2.prev = node1
                return True
        else:
            node1.next = self.head
            node1.prev = self.head.prev
            self.head.prev.next = node1
            self.head.prev = node1
            return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        node = self.head.next
        while node != self.head:
            if node.item == item:
                node.prev.next = node.next
                node.next.prev = node.prev
                return True
            elif node.item < item:
                node = node.next
            elif node.item > item:
                return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index = 0
        node1 = self.head.next
        while node1 != self.head:
            if node1.item == item:
                return index
            else:
                index += 1
                node1 = node1.next
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        index1 = 0
        node1 = self.head.next
        if index < 0:
            raise IndexError
        while node1 != self.head:
            if index1 == index:
                temp = node1.item
                node1.prev.next = node1.next
                node1.next.prev = node1.prev
                return temp
            else:
                node1 = node1.next
                index1 += 1
        else:
            raise IndexError

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.helper_search_1(self.head.next, item)

    def helper_search_1(self, node1, item):
        if node1.item == item:
            return True
        elif node1 == self.head.prev:
            return False
        elif node1.item > item:
            return False
        return self.helper_search_1(node1.next, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        list1 = []
        node1 = self.head.next
        while node1 != self.head:
            list1.append(node1.item)
            node1 = node1.next
        return list1

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.helper_python_l_r_1(self.head.prev)

    def helper_python_l_r_1(self, node1):
        if node1 == self.head:
            return []
        return [node1.item] + self.helper_python_l_r_1(node1.prev)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_help_1(self.head.next)

    def size_help_1(self, node1):
        if node1 == self.head:
            return 0
        return 1 + self.size_help_1(node1.next)
