from algorithms.pathfinding import BFS
from graphlib.graph import Graph
from graphlib.utils import create_normal_graph_and_without_red

"""
If a path with no red vertices from S to T does NOT exist, but there exists a path, it means that that path has 
at least 1 red vertex.

Solves only instances of graphs that return -1 for the None problem - so only graphs with no paths with no red vertices.
"""

class Some_Using_None:

    def solve(graph: Graph, graph_without_red: Graph):
        path, pathExists = BFS().find_path(graph_without_red.source, graph_without_red.sink,
                                           graph_without_red.getNumNodes())

        if not pathExists:
            path, pathExists = BFS().find_path(graph.source, graph.sink,
                                               graph.getNumNodes())
            if pathExists:
                print("True")
            else:
                print("False")
        else:
            print("Unsolvable")
