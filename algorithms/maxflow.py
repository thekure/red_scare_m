# This Ford-Fulkerson implementation was taken from Silke and Rakuls Bachelors project.

from graphlib.graph import Graph
from algorithms.pathfinding import BFS, DFS


class MaxFlow:

    """Ford fulkerson that uses BFS as default"""

    def fordFulkerson(graph: Graph, find_from, find_to, pathfinder=BFS()):
        maxFlow = 0
        num_nodes = graph.getNumNodes()

        path, isPath = pathfinder.find_path(find_from, find_to, num_nodes)

        while isPath:
            bottle = 9223372036854775807
            v = find_to

            while v.id is not find_from.id:
                bottle = min(bottle, path.get(v.id).residualCapacityTo(v))
                v = path.get(v.id).getOther(v)

            v = find_to
            while v.id is not find_from.id:
                path.get(v.id).addResidualFlowTo(bottle, v)
                v = path.get(v.id).getOther(v)

            maxFlow += bottle

            path, isPath = pathfinder.find_path(find_from, find_to, num_nodes)

        return maxFlow
