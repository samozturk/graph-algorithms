import priority_dict
from graph import *

def spanning_tree(graph):

    # Holds a mapping from a pair of edges to the edge weight
    # The edge weight is the priority of the edge
    priority_queue = priority_dict.priority_dict()

    for v in range(graph.numVertices):
        for neighbor in graph.get_adjacent_vertices(v):

            priority_queue[(v, neighbor)] = graph.get_edge_weight(v, neighbor)

        visited_vertices = set()

        # Maps a node to all its adjacent nodes which are in the minimum spanning tree
        spanning_tree = {}

        for v in range(graph.numVertices):
            spanning_tree[v] = set()

        # Number of edges we have got so far
        num_edges = 0

        while len(priority_queue.keys()) > 0 and num_edges < graph.numVertices - 1):
            v1, v2 = priority_queue.pop_smallest()

            if v1 in spanning_tree[v2]:
                continue

            # Arrange the spanning tree so the node with the smaller vertex id is always first.
            # This greatly simplifies the code to find cycles in this tree.
            vertex_pair = sorted([v1, v2])

            spanning_tree[vertex_pair[0]].add(vertex_pair[1])

            # Check if adding the current edge causes a cycle
            if has_cycle(spanning_tree):
                spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
                continue
            num_edges = num_edges + 1
            
            visited_vertices.add(v1)
            visited_vertices.add(v2)

            print("Visited vertices: ", visited_vertices)

            if len(visited_vertices) != graph.numVertices:
                print("Minimum spanning tree not found.")
            else:
                print("Minimum spanning tree:")
                for key in spanning_tree:
                    for value in spanning_tree[key]:
                        print(key, "-->", value)

            
            def has_cycle(spanning_tree):
                for source in spanning_tree:
                    q = []
                    q.append(source)

                    visited_vertices = set()
                    while len(q) > 0:
                        vertex = q.pop(0)

                        # If we've see the vertex before in this spanning tree there is a cycle!
                        if vertex in visited_vertices:
                            return True

                        visited_vertices.add(vertex)

                        # Add al vertices connected by edges in this spanning tree
                        q.extend(spanning_tree[vertex])
                return False




