from shortest_path import shortest_path
from topological_sort import topological_sort
from graph import AdjacencyMatrixGraph, AdjacencySetGraph


g = AdjacencySetGraph(4, directed=False)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to :", i, g.get_adjacent_vertices(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print('Edge weight:', i, " ", j, "weight: ", g.get_edge_weight(i, j))

g.display()


g_topsort = AdjacencyMatrixGraph(9, directed=True)
g_topsort.add_edge(0,1)
g_topsort.add_edge(1,2)
g_topsort.add_edge(2,7)
g_topsort.add_edge(2,4)
g_topsort.add_edge(2,3)
g_topsort.add_edge(1,5)
g_topsort.add_edge(5,6)
g_topsort.add_edge(3,6)
g_topsort.add_edge(3,4)
g_topsort.add_edge(6,8)

topological_sort(g_topsort)

g_short_path = AdjacencySetGraph(8, directed=False)
g_short_path.add_edge(0,1)
g_short_path.add_edge(1,2)
g_short_path.add_edge(1,3)
g_short_path.add_edge(2,3)
g_short_path.add_edge(1,4)
g_short_path.add_edge(3,5)
g_short_path.add_edge(5,4)
g_short_path.add_edge(3,6)
g_short_path.add_edge(6,7)
g_short_path.add_edge(0,7)

shortest_path(g_short_path, 0, 5)