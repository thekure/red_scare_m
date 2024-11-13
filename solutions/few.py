from sys import maxsize

from algorithms.pathfinding import BinaryBFS
from graphlib.graph import Graph
from graphlib.utils import create_weighted_graph_based_on_reds

class Few:

    def solve(graph: Graph):
        dist = 1 if graph.source.isRed else 0
        dist += BinaryBFS().find_path(graph)

        if dist != maxsize: print(dist)
        else: print(-1)