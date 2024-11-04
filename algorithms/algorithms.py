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
    

class NoneOrSome:
    """ Finds a path from S to T using BFS
        The graph given to none() must be a none graph for this to work
    """
    def none(graph: Graph, pathfinder=BFS()):
        num_nodes = graph.getNumNodes()
        path, isPath = pathfinder.find_path(graph.source, graph.sink, num_nodes)

        if not isPath:
            # if there is no path from s to t
            print(f"-1")
        else:
            # otherwise a path exists and we need to find the length of it
            v = graph.sink
            length = 0
            while v.id is not graph.source.id:
                length += 1
                v = path.get(v.id).getOther(v)
            print(f"{length}")


    """ The only way I was able to solve this, was to find all paths from S to T and filter them to only contain the one that has at least one red vertex in them.
        I'm unsure whether or not this solution runs in polynomial time, but I don't know how to solve it differently
    """
    def some(graph: Graph, pathfinder=DFS()):
        all_paths = pathfinder.find_all_paths(graph.source, graph.sink)
        filtered_path = {key: value for key, value in all_paths.items() if key is True}

        if len(filtered_path) == 1:
            print(True)
        else:
            print(False)
        
