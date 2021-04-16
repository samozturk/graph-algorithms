import priority_dict
from graph import *

def spanning_tree(graph, source):
    # A dictionary mapping from the vertex number to a tuple of
    # (distance from the source, last vertex on path from source)
    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)
    
    # The distance to the source from itself is 0
    distance_table[source] = (0, source)

    # Hold mapping of vertex id to distance from source
    # Access the highest priority (lowest distance) item first

    priority_queue = priority_dict.priority_dict()
    priority_queue[source] = 0

    visited_vertices = set()

    # Set of edges where each edge is represented as a string
    # "1->2": is an edge between vertices 1 and 2
    spanning_tree = set()

    while len(priority_queue.keys()) > 0:
        current_vertex = priority_queue.pop_smallest()

        # If we've visited a vertex earlier then we have all
        # outbound edges from it, we do not process it again
        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)

        # If the current vertex is the source, we haven't traversed an
        # edge yet, no edge to add to our spanning tree
        if current_vertex != source:
            # The current vertex is connected by the lowest weighted edge
            last_vertex = distance_table[current_vertex][1]
            edge = str(last_vertex) + '-->' + str(current_vertex)

            if edge not in spanning_tree:
                spanning_tree.add(edge)
        
        for neighbor in graph.get_adjacent_vertices(current_vertex):
            
            # The distance to the neighbor is only the weight of the edge connection to the neighbor
            distance = graph.get_edge_weight(current_vertex, neighbor)

            # The last recorded distance of this neighbor
            neighbor_distance = distance_table[neighbor][0]

            # If this neighbor has been seen for the first time or the new edge
            # connecting this neighbor is of a lower weight than the last
            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)
                priority_queue[neighbor] = distance

    for edge in spanning_tree:
        print(edge)


