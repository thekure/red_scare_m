from graphlib.graph import Graph
from algorithms.pathfinding import BFS, DFS


class MaxFlow:

    """Ford fulkerson that uses BFS as default"""

    def fordFulkerson(graph: Graph, pathfinder=BFS()):
        maxFlow = 0
        num_nodes = graph.getNumNodes()

        path, isPath = pathfinder.find_path(graph.source, graph.sink, num_nodes)

        while isPath:
            bottle = 9223372036854775807
            v = graph.sink

            while v.id is not graph.source.id:
                bottle = min(bottle, path.get(v.id).residualCapacityTo(v))
                v = path.get(v.id).getOther(v)

            v = graph.sink
            while v.id is not graph.source.id:
                path.get(v.id).addResidualFlowTo(bottle, v)
                v = path.get(v.id).getOther(v)

            maxFlow += bottle

            path, isPath = pathfinder.find_path(graph.source, graph.sink, num_nodes)

        return maxFlow

        

class Alternating:
    """ Performs a BFS while alternating between black / red nodes
    """
    def alternating(graph: Graph, pathfinder=BFS()):
        num_nodes = graph.getNumNodes()
        path, isPath = pathfinder.find_alternating_path(graph.source, graph.sink, num_nodes)

        if not isPath:
            print("False")
        else:
            print(isPath)

        # -- the following is just for printing the path that was found - useful for debugging
        # for edge in path.values():
        #     edge.printEdge()