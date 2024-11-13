from graphlib.graph import Graph
from algorithms.pathfinding import BFS

class Alternating:
    """ Performs a BFS while alternating between black / red nodes
    """
    def solve(graph: Graph, pathfinder=BFS()):
        num_nodes = graph.getNumNodes()
        path, isPath = pathfinder.find_alternating_path(graph.source, graph.sink, num_nodes)

        if not isPath:
            print("False")
        else:
            print(isPath)

        # -- the following is just for printing the path that was found - useful for debugging
        # for edge in path.values():
        #     edge.printEdge()