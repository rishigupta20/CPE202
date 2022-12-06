from sys import argv
from stack_array import *


class Vertex:
    def __init__(self, in_degree, adjacency_list):
        '''Add whatever parameters/attributes are needed'''
        self.in_degree = in_degree
        self.adjacency_list = adjacency_list


def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    dictionary = {}
    if len(vertices) == 0:
        raise ValueError('input contains no edges')
    if len(vertices) % 2 != 0:
        raise ValueError('input contains an odd number of tokens')
    for val in vertices:
        dictionary[val] = Vertex(0, [])
    for idx in range(0, len(vertices), 2):
        dictionary[vertices[idx + 1]].in_degree += 1
        dictionary[vertices[idx]].adjacency_list.append(vertices[idx + 1])
    stack = Stack(len(dictionary))
    output = ''
    for val1 in dictionary:
        if dictionary[val1].in_degree == 0:
            stack.push(val1)
    while stack.is_empty() is False:
        val2 = stack.pop()
        output += val2
        output += '\n'
        for vert in dictionary[val2].adjacency_list:
            dictionary[vert].in_degree -= 1
            if dictionary[vert].in_degree == 0:
                stack.push(vert)
        del dictionary[val2]
    if len(dictionary) > 0:
        raise ValueError('input contains a cycle')
    return output


# 100% Code coverage NOT required
def main():
    """Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG.  Use this code
       if you want to run tests on a file with a list of edges"""
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
