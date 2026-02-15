# graphs are the structures that model relationships
class Graph:
    def __init__ (self, directed=False ):
        
        self.graph = {} # this uses the adjacency list rep
        self.derected = derected # directed is a one way connection

    def add_vertex (self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    # use 2 vertex to define the edge e.g from A to B
    def add_edge (self, vertex1, vertex2, weight=1):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        if not self.directed:
          self.graph[vertex2].append((vertex1, weight))
