from sys import maxsize

from algorithms.pathfinding import BinaryBFS
from graphlib.utils import create_weighted_graph_based_on_reds

def few_graph():
    graph = create_weighted_graph_based_on_reds()
    dist = 1 if graph.source.isRed else 0
    dist += BinaryBFS().find_path(graph)
    return dist if dist != maxsize else -1

print(few_graph())