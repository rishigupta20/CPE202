from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = float(key)
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        if self.root is None:
            return True
        return False

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return False
        return self.search_helper(self.root, key)

    def search_helper(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if node.key > key:
            return self.search_helper(node.left, key)
        if node.key < key:
            return self.search_helper(node.right, key)

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        node = TreeNode(key, data)
        if self.is_empty():
            self.root = node
        else:
            return self.insert_helper(self.root, node)

    def insert_helper(self, c_n, n_n):
        if c_n.key == n_n.key:
            c_n.data = n_n.data
        elif c_n.key < n_n.key:
            if c_n.right is None:
                c_n.right = n_n
            else:
                self.insert_helper(c_n.right, n_n)
        elif c_n.key > n_n.key:
            if c_n.left is None:
                c_n.left = n_n
            else:
                self.insert_helper(c_n.left, n_n)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.helper_find_min(self.root)

    def helper_find_min(self, node):
        if node.left is None:
            return node.key, node.data
        else:
            return self.helper_find_min(node.left)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.helper_find_max(self.root)

    def helper_find_max(self, node):
        if node.right is None:
            return node.key, node.data
        else:
            return self.helper_find_max(node.right)

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.helper_tree_height(self.root)

    def helper_tree_height(self, node):
        left_height = 0
        right_height = 0
        if node.left is None and node.right is None:
            return 0
        if node.left is not None:
            left_height = 1 + self.helper_tree_height(node.left)
        if node.right is not None:
            right_height = 1 + self.helper_tree_height(node.right)
        if left_height > right_height:
            return left_height
        else:
            return right_height

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        inorder_list = []
        if self.is_empty():
            return inorder_list
        self.helper_inorder_list(self.root, inorder_list)
        return inorder_list

    def helper_inorder_list(self, node, inorder_list):
        if node is None:
            return
        self.helper_inorder_list(node.left, inorder_list)
        inorder_list.append(node.key)
        self.helper_inorder_list(node.right, inorder_list)

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        preorder_list = []
        if self.is_empty():
            return preorder_list
        self.helper_preorder_list(self.root, preorder_list)
        return preorder_list

    def helper_preorder_list(self, node, preorder_list):
        if node is None:
            return
        preorder_list.append(node.key)
        self.helper_preorder_list(node.left, preorder_list)
        self.helper_preorder_list(node.right, preorder_list)

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000)  # Don't change this!
        level_order_list = []
        if self.is_empty():
            return level_order_list
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            level_order_list.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return level_order_list
