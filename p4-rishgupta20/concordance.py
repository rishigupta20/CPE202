from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        self.stop_table = HashTable(191)
        for line in f:
            if line[-1:] == "\n":
                self.stop_table.insert(line[:-1])
            else:
                self.stop_table.insert(line)
        f.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, 'r')
        except:
            raise FileNotFoundError
        self.concordance_table = HashTable(191)
        counter = 1
        for line in f:
            line = line.lower()
            line = line.replace("'", "")
            for s in string.punctuation:
                line = line.replace(s, " ")
            list_of_words = line.split()
            set_words = set(list_of_words)
            for tok in set_words:
                if tok.isalpha():
                    if self.stop_table.in_table(tok):
                        continue
                    if self.concordance_table.in_table(tok):
                        self.concordance_table.insert(tok, self.concordance_table.get_value(tok) + " " + str(counter))
                    else:
                        self.concordance_table.insert(tok, str(counter))
            counter += 1
        f.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        output = open(filename, 'w')
        final = self.concordance_table.get_all_keys()
        final.sort()
        output.write(final[0] + ": " + self.concordance_table.get_value(final[0]))
        for val in final[1:]:
            output.write("\n")
            output.write(val + ": " + self.concordance_table.get_value(val))
        output.close()
