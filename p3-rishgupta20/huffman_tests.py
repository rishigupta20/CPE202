import unittest
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertEqual(freqlist[0], 0)
        self.assertListEqual(freqlist[97:104], anslist)

    def test_cnt_freq1(self):
        freqlist = cnt_freq("empty.txt")
        anslist = [0] * 256
        self.assertEqual(freqlist[200], 0)
        self.assertListEqual(freqlist, anslist)

    def test_cnt_freq2(self):
        with self.assertRaises(FileNotFoundError):
            cnt_freq('p.txt')

    def test_lt_and_eq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        self.assertEqual(freqlist[12], 0)
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(ascii, freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(freqlist[56], 0)
        self.assertEqual(lst.index(HuffmanNode(101, 0)), 0)
        self.assertEqual(lst.index(HuffmanNode(100, 16)), 6)
        self.assertEqual(lst.index(HuffmanNode(97, 2)), 2)
        self.assertIsNone(HuffmanNode(97, 2))

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(freqlist[6], 0)
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_huff_tree1(self):
        freqlist = cnt_freq("empty.txt")
        self.assertEqual(freqlist[99], 0)
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree, None)

    def test_create_huff_tree_2(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(freqlist[1], 0)
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)
        left2 = left.left
        self.assertEqual(left2.freq, 8)
        self.assertEqual(left2.char, 97)
        left3 = left2.left
        self.assertEqual(left3.freq, 4)
        self.assertEqual(left3.char, 97)
        left4 = left3.left
        self.assertEqual(left4.freq, 2)
        self.assertEqual(left4.char, 97)
        leftr1 = left.right
        self.assertEqual(leftr1.freq, 8)
        self.assertEqual(leftr1.char, 99)
        leftr2 = left2.right
        self.assertEqual(leftr2.freq, 4)
        self.assertEqual(leftr2.char, 98)
        leftr3 = left3.right
        self.assertEqual(leftr3.freq, 2)
        self.assertEqual(leftr3.char, 102)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(freqlist[97], 2)
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_header1(self):
        freqlist = cnt_freq("empty.txt")
        self.assertEqual(freqlist[0], 0)
        self.assertEqual(create_header(freqlist), "")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(freqlist[0], 0)
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_create_code1(self):
        freqlist = cnt_freq("one_unique.txt")
        self.assertEqual(freqlist[43], 0)
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_03_textfile(self):
        huffman_encode("empty.txt", "empty_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_out.txt empty_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb empty_out_compressed.txt empty_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_04_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_05_textfile(self):
        huffman_encode("one_unique.txt", "one_unique_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb one_unique_out.txt one_unique_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb one_unique_out_compressed.txt one_unique_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_06_textfile(self):
        huffman_encode("single_unique.txt", "single_unique_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb single_unique_out.txt single_unique_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb single_unique_out_compressed.txt single_unique_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_parse_header(self):
        header_string = '97 3 98 4 99 2 100 5'
        ansList = [3, 4, 2, 5]
        test = parse_header(header_string)
        self.assertEqual(test[8], 0)
        self.assertEqual(test[97:101], ansList)

    def test_parse1_header(self):
        header_string = '2 4 3 10 4 99'
        ansList = [4, 10, 99]
        test = parse_header(header_string)
        self.assertEqual(test[251], 0)
        self.assertEqual(test[2:5], ansList)

    def test_parse2_header(self):
        header_string = '2 4 3 10 4 99 6 999'
        ansList = [4, 10, 99, 0, 999]
        test = parse_header(header_string)
        self.assertEqual(test[0], 0)
        self.assertEqual(test[2:7], ansList)

    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def test_02a_test_file1_parse_header(self):
        f = open('empty_compressed_soln.txt', 'rb')
        header = f.readline()
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_02_test_empty_decode(self):
        huffman_decode("file2_compressed_soln.txt", "file2_decoded.txt")
        err = subprocess.call("diff -wb file2.txt file2_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_03_test_empty_decode(self):
        huffman_decode("empty_compressed_soln.txt", "empty_decoded.txt")
        err = subprocess.call("diff -wb empty.txt empty_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_04_test_empty_decode(self):
        huffman_decode("declaration_compressed_soln.txt", "declaration_decoded.txt")
        err = subprocess.call("diff -wb declaration.txt declaration_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_05_test_empty_decode(self):
        huffman_decode("one_unique_compressed_soln.txt", "one_unique_decoded.txt")
        err = subprocess.call("diff -wb one_unique.txt one_unique_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_06_test_empty_decode(self):
        huffman_decode("multiline_compressed_soln.txt", "multiline_decoded.txt")
        err = subprocess.call("diff -wb multiline.txt multiline_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_07_test_empty_decode(self):
        huffman_decode("single_unique_compressed_soln.txt", "single_unique_decoded.txt")
        err = subprocess.call("diff -wb single_unique.txt single_unique_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_08_test_empty_decode(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode('p.txt', 'l.txt')

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)


if __name__ == '__main__':
    unittest.main()
