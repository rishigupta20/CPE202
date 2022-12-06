from ordered_list import *

from huffman_bit_writer import *

from huffman_bit_reader import *


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the frequency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return type(other) == HuffmanNode and self.char == other.char and self.freq == other.freq

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq == other.freq:
            return self.char < other.char
        return self.freq < other.freq


def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    try:
        f = open(filename, 'r')
    except:
        raise FileNotFoundError
    l = [0] * 256
    for line in f:
        for char in line:
            var = ord(char)
            l[var] += 1
    f.close()
    return l


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    l = OrderedList()
    for idx in range(len(char_freq)):
        if not char_freq[idx] == 0:
            l.add(HuffmanNode(idx, char_freq[idx]))
    while l.size() > 1:
        temp1 = l.pop(0)
        temp2 = l.pop(0)
        if temp1.char < temp2.char:
            temp3 = HuffmanNode(temp1.char, temp1.freq + temp2.freq)
        else:
            temp3 = HuffmanNode(temp2.char, temp1.freq + temp2.freq)
        temp3.left = temp1
        temp3.right = temp2
        l.add(temp3)
    if l.is_empty():
        return None
    return l.pop(0)


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    l = [''] * 256
    code = ''
    if node is None:
        return l
    return helper_create_code(node, l, code)


def helper_create_code(node, l, code):
    if node.left is None and node.right is None:
        l[node.char] = code
    else:
        helper_create_code(node.left, l, code + '0')
        helper_create_code(node.right, l, code + '1')
    return l


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    header = ''
    for idx in range(len(freqs)):
        if not freqs[idx] == 0:
            header += ' ' + str(idx) + ' ' + str(freqs[idx])
    return header[1:]


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    freq = cnt_freq(in_file)
    tree_node = create_huff_tree(freq)
    code = create_code(tree_node)
    header = create_header(freq)
    infile = open(in_file, 'r')
    data = infile.read()
    outfile = open(out_file, 'w')
    if len(data) == 0:
        infile.close()
        outfile.close()
        outfile_compress = out_file[0:len(out_file) - 4] + '_compressed.txt'
        compress = HuffmanBitWriter(outfile_compress)
        compress.close()
        return
    outfile.write(header + '\n')
    encoded_str = ''
    for char in data:
        encoded_str += code[ord(char)]
    outfile.write(encoded_str)
    infile.close()
    outfile.close()
    outfile_compress = out_file[0:len(out_file) - 4] + '_compressed.txt'
    compress = HuffmanBitWriter(outfile_compress)
    compress.write_str(header + '\n')
    compress.write_code(encoded_str)
    compress.close()


def huffman_decode(encoded_file, decode_file):
    try:
        f = open(encoded_file, 'r')
        f.close()
    except:
        raise FileNotFoundError
    f1 = open(decode_file, 'w')
    file = HuffmanBitReader(encoded_file)
    header = file.read_str()
    l = parse_header(header)
    tree = create_huff_tree(l)
    root_node = tree
    total = sum(l)
    if tree is None:
        f1.close()
        file.close()
        return
    if tree.left is not None and tree.right is not None:
        i = 0
        while i <= total:
            try:
                var = file.read_bit()
            except:
                break
            if tree.left is None and tree.right is None:
                f1.write(chr(tree.char))
                tree = root_node
                i += 1
            if var is False:
                tree = tree.left
            if var is True:
                tree = tree.right
    else:
        f1.write(chr(tree.char) * int(tree.freq))
    f1.close()
    file.close()


def parse_header(header_string):
    header = header_string.split()
    l = [0] * 256
    for i in range(0, len(header) - 1, 2):
        char = int(header[i])
        freq = int(header[i + 1])
        l[char] = freq
    return l
