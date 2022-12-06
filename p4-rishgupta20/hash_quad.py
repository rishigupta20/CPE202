import math


class HashTable:

    def __init__(self, table_size):  # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will
            be used, if 11 is passed, 11 will be used.)'''
        if self.is_prime(table_size):
            self.table_size = table_size
        else:
            self.table_size = self.next_prime(table_size)
        self.num_items = 0
        self.hash = [None] * self.table_size
        self.rehash = []

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0
        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                self.hash[hash_value][1] = value
                return
            i += 1
            hash_value = start + (i ** 2)
            while hash_value > self.table_size - 1:
                hash_value = hash_value - self.table_size
        self.hash[hash_value] = [key, value]
        self.num_items += 1
        if self.get_load_factor() > 0.5:
            self.helper_insert()

    def helper_insert(self):
        original = self.hash
        self.table_size = self.table_size * 2
        if self.is_prime(self.table_size) is False:
            self.table_size = self.next_prime(self.table_size)
        self.hash = [None] * self.table_size
        self.num_items = 0
        for val in original:
            if val is not None:
                self.insert(val[0], val[1])

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        n = min(8, len(key))
        hash_value = 0
        for idx in range(n):
            hash_value += ord(key[idx]) * 31 ** (n - 1 - idx)
        return hash_value

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def next_prime(self, n):
        if n <= 1:
            return 2
        prime_val = n
        found = False
        while not found:
            prime_val = prime_val + 1
            if self.is_prime(prime_val):
                found = True
        return prime_val

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0
        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                return True
            else:
                i += 1
                hash_value = start + (i ** 2)
                while hash_value > self.table_size - 1:
                    hash_value = hash_value - self.table_size
        return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0
        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                return hash_value
            else:
                i += 1
                hash_value = start + (i ** 2)
                while hash_value > self.table_size - 1:
                    hash_value = hash_value - self.table_size
        return None

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        get_all_keys = []
        for val in self.hash:
            if val is not None:
                get_all_keys.append(val[0])
        return get_all_keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0import math


class HashTable:

    def __init__(self, table_size):  # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will
            be used, if 11 is passed, 11 will be used.)'''
        if self.is_prime(table_size):
            self.table_size = table_size
        else:
            self.table_size = self.next_prime(table_size)
        self.num_items = 0
        self.hash = [None] * self.table_size
        self.rehash = []

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0
        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                self.hash[hash_value][1] = value
                return
            i += 1
            hash_value = start + (i ** 2)
            while hash_value > self.table_size - 1:
                hash_value = hash_value - self.table_size
        self.hash[hash_value] = [key, value]
        self.num_items += 1
        if self.get_load_factor() > 0.5:
            self.helper_insert()

    def helper_insert(self):
        original = self.hash
        self.table_size = self.table_size * 2
        if self.is_prime(self.table_size) is False:
            self.table_size = self.next_prime(self.table_size)
        self.hash = [None] * self.table_size
        self.num_items = 0
        for val in original:
            if val is not None:
                self.insert(val[0], val[1])

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        n = min(8, len(key))
        hash_value = 0
        for idx in range(n):
            hash_value += ord(key[idx]) * 31 ** (n - 1 - idx)
        return hash_value

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def next_prime(self, n):
        if n <= 1:
            return 2
        prime_val = n
        found = False
        while not found:
            prime_val = prime_val + 1
            if self.is_prime(prime_val):
                found = True
        return prime_val

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0
        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                return True
            else:
                i += 1
                hash_value = start + (i ** 2)
                while hash_value > self.table_size - 1:
                    hash_value = hash_value - self.table_size
        return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0
        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                return hash_value
            else:
                i += 1
                hash_value = start + (i ** 2)
                while hash_value > self.table_size - 1:
                    hash_value = hash_value - self.table_size
        return None

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        get_all_keys = []
        for val in self.hash:
            if val is not None:
                get_all_keys.append(val[0])
        return get_all_keys

    def get_value(self, key):
        ''' Returns the value associated with the key.
        If key is not in hash table, returns None.'''
        hash_value = self.horner_hash(key) % self.table_size
        start = hash_value
        i = 0
        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                return self.hash[hash_value][1]
            else:
                i += 1
                hash_value = start + (i ** 2)
                while hash_value > self.table_size - 1:
                    hash_value = hash_value - self.table_size
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size

        while self.hash[hash_value] is not None:
            if self.hash[hash_value][0] == key:
                return self.hash[hash_value][1]
            else:
                i += 1
                hash_value = start + (i ** 2)
                while hash_value > self.table_size - 1:
                    hash_value = hash_value - self.table_size
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size
