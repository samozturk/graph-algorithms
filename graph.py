import abc
import numpy as np

class Graph(abc.ABC):
    def __init__(self, numVertices, directed=False):
        self.numVertices =  numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
            
        self.matrix = np.zeros((numVertices, numVertices))
        
    def add_edge(self, v1, v2, weight=1):
        # Ensure numVertices is between 0 and numVertices
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" %(v1, v2))
        # Sanity check
        if weight < 1:
            raise ValueError("An edge cannot have weight less than 1!")
        # Declare weight(which is 1 by default in undirected graphs)
        self.matrix[v1][v2] = weight
        # For undirected graph, adjacency matrix is symetric.
        if self.directed == False:
            self.matrix[v2][v1] = weight
            
    def get_adjacent_vertices(self, v):
        # Check whether v is a valid vertex
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" %v)
        # Initialize empty list of adjacent_vertices to populate
        adjacent_vertices = []
        # Itarete through all other nodes in the adjacency matrix larger than 0 and return list
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

        # Get degree of a vertex
    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" %v)

        indegree =  0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1
            
        return indegree
        
    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)



class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)

        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and % d are out of bounds" % (v1,v2))
        
        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weight > 1")
        
        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2]. add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertext %d" %v)

        indegree = 0

        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "---->", v)



 