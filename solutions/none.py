from algorithms.pathfinding import BFS
from graphlib.utils import *

class _None:
    def solve(graph: Graph):
        debug = False

        path, pathExists = BFS().find_path(graph.source, graph.sink, graph.getNumNodes())

        if debug:
            for edge in path.values():
                print(edge.printEdge())

        if pathExists:
            length = 0
            current_node = graph.sink
            while current_node != graph.source:
                if debug: print(current_node.id)
                length += 1
                edge = path.get(current_node.id)
                current_node = edge.getOther(current_node)
            print(length)
        else:
            print(-1)
