from algorithms.pathfinding import BFS, DFS
from graphlib.utils import create_graphs_without_sink_and_without_source

"""
The idea of this solution is to first find a path from the source to all red vertices, going through them one by 
one, then from the current red vertex to sink, and stop if 2 paths are found for the same red vertex.
This works for DAG (Directed Acyclic Graphs)
For an Undirected Acyclic Graph (tree) => one or no path at all between source and sink => use BFS
+ Easiest scenario: For all graphs, if a path exists from s to t and s or t are red => True
"""

class Some:

    def solve(graph_original, graph_without_sink, graph_without_source):
        # easiest scenario
        path, exists = BFS().find_path(graph_original.source, graph_original.sink, graph_original.getNumNodes())

        if exists and (graph_original.source.isRed or graph_original.sink.isRed):
            print("True")
            return

        if graph_original.type == "directed":
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
                            print("True")
                            found = True
                            break

            if not found:
                print("False")

        elif graph_original.type == "undirected" and DFS().is_acyclic(graph_original):
            path, exists = BFS().find_path(graph_original.source, graph_original.sink, graph_original.getNumNodes())

            if exists:
                reds = 1 if graph_original.source.isRed else 0
                current_node = graph_original.sink
                while current_node != graph_original.source:
                    reds += 1 if current_node.isRed else 0
                    edge = path.get(current_node.id)
                    current_node = edge.getOther(current_node)
                if reds != 0:
                    print("True")
                else:
                    print("False")
            else:
                print("False")

        else:
            print("NP-hard")
