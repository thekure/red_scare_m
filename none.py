from algorithms.pathfinding import BFS
from graphlib.utils import *
from algorithms.maxflow import MaxFlow

graph = create_graph_without_red()
# graph.printGraph()
path, pathExists = BFS().find_path(graph.source, graph.sink, graph.getNumNodes())

for edge in path.values():
    print(edge.printEdge())

if pathExists:
    length = 0
    current_node = graph.sink
    while current_node != graph.source:
        print(current_node.id)
        length += 1
        edge = path.get(current_node.id)
        current_node = edge.getOther(current_node)
    print(length)
else:
    print(-1)

