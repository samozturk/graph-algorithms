from queue import Queue
from graph import *

def topological_sort(graph):
    queue = Queue()
    indegreeMap = {}

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)

        # Queue all nodes which have no dependencies i.e.
        # no edges coming in
        if indegreeMap[i] == 0:
            queue.put(i)

    sortedList = []
    while not queue.empty():
        vertex = queue.get()
        sortedList.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] = indegreeMap[v] - 1

            if indegreeMap[v] == 0:
                queue.put(v)

    if len(sortedList) != graph.numVertices:
        raise ValueError("This graph has a cycle!")

    print(sortedList)

