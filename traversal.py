from queue import Queue
from graph import * 

def breadth_first(graph, start=0):

    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue
        print('Visit: ', vertex)

        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)

def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return

    visited[current] = 1

    print("Visit: ", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)
        


    