from algorithms.pathfinding import BFS
from graphlib.utils import create_graphs_without_sink_and_without_source

"""
The idea of this solution is to first find a path from the source to all red vertices, going through them one by 
one, then from the current red vertex to sink, and stop if 2 paths are found for the same red vertex.
However, this approach allows a vertex to be visited more than once in a path.
If this is not allowed, a solution for this would make it, most probably, exponential :(
"""

class Some_Idea:

    def solve(graph_without_sink, graph_without_source):

        found = False
        for node in graph_without_sink.dictOfNodes.values():
            # Skip non-red nodes and source/sink
            if node.isRed and node.id != graph_without_sink.source.id and node.id != graph_without_source.sink.id:
                path_source_to_red, pathExists_source_to_red = BFS().find_path(graph_without_sink.source, node,
                                                                               graph_without_sink.getNumNodes())
                if pathExists_source_to_red:
                    # Get Node from other graph (possible different outgoing edges)
                    node_other_graph = graph_without_source.dictOfNodes.get(node.id)
                    path_red_to_sink, pathExists_red_to_sink = BFS().find_path(node_other_graph, graph_without_source.sink,
                                                                               graph_without_source.getNumNodes())
                    if pathExists_red_to_sink:
                        print("Solution found through Node : " + node.id)
                        found = True
                        break

        if not found:
            print("No solution")
