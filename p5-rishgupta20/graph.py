from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each Qedge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        self.copy = []
        self.graph = {}
        f = open(filename, 'r')
        for line in f:
            line = line.split()
            self.add_vertex(line[0])
            self.add_vertex(line[1])
            self.add_edge(line[0], line[1])
        f.close()

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)
            self.copy.append(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key not in self.graph:
            return None
        return self.graph[key]

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        get_vertices_list = sorted(list(self.graph))
        return get_vertices_list

    def conn_components(self):
        '''Return a Python list of lists.  For example: if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        # This method MUST use Depth First Search logic!
        stack = Stack(len(self.graph) * 999)
        result = []
        start = 0
        component = []
        visited = {}
        while start < len(self.graph):
            stack.push(self.copy[start])
            while not stack.is_empty():
                v1 = stack.pop()
                if v1 not in visited:
                    start += 1
                    for vert in self.graph[v1].adjacent_to:
                        stack.push(vert)
                    visited[v1] = v1
                    component.append(v1)
            component.sort()
            result.append(component)
            component = []
            visited = {}
        result.sort()
        return result

    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        # This method MUST use Breadth First Search logic!
        queue = Queue(len(self.graph))
        color = {}
        for val in self.graph:
            if val not in color:
                color[val] = 'red'
                queue.enqueue(val)
                while not queue.is_empty():
                    var = queue.dequeue()
                    if color[var] == 'red':
                        for vert in self.graph[var].adjacent_to:
                            if vert not in color:
                                color[vert] = 'black'
                                queue.enqueue(vert)
                            elif color[vert] == 'black':
                                continue
                            elif color[vert] == 'red':
                                return False
                    elif color[var] == 'black':
                        for vert in self.graph[var].adjacent_to:
                            if vert not in color:
                                color[vert] = 'red'
                                queue.enqueue(vert)
                            elif color[vert] == 'red':
                                continue
                            elif color[vert] == 'black':
                                return False
        return True
