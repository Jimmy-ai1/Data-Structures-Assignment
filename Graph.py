# graphs are the structures that model relationships
from collections import deque
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
    # depth first search - basically going as deep as possible without backtracking
    def dfs (self, start):

        visited = set()
        result = []

        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            # the _ skips the weight
            for neighbor, _ in self.graph.get(vertex, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        dfs_helper(start)
        return result

    #Breadth first  search
    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vrtex)

            for neighbor, _ in self.graph.get(vertex, []):
                if neighbornot in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result
