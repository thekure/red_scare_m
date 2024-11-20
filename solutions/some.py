from algorithms.pathfinding import BFS, DFS
from graphlib.utils import create_graphs_without_sink_and_without_source
from graphlib.graph import Graph, Node, Edge
from algorithms.maxflow import MaxFlow

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
        if graph_original.source.isRed or graph_original.sink.isRed:
            path, exists = BFS().find_path(
                graph_original.source, graph_original.sink, graph_original.getNumNodes()
            )

            if exists:
                print("True")
                return

        if graph_original.type == "directed":
            found = False
            for node in graph_without_sink.dictOfNodes.values():
                # Skip non-red nodes and source/sink
                if (
                    node.isRed
                    and node.id != graph_without_sink.source.id
                    and node.id != graph_without_source.sink.id
                ):
                    path_source_to_red, pathExists_source_to_red = BFS().find_path(
                        graph_without_sink.source,
                        node,
                        graph_without_sink.getNumNodes(),
                    )
                    if pathExists_source_to_red:
                        # Get Node from other graph (possible different outgoing edges)
                        node_other_graph = graph_without_source.dictOfNodes.get(node.id)
                        path_red_to_sink, pathExists_red_to_sink = BFS().find_path(
                            node_other_graph,
                            graph_without_source.sink,
                            graph_without_source.getNumNodes(),
                        )
                        if pathExists_red_to_sink:
                            print("True")
                            found = True
                            break

            if not found:
                print("False")

        elif graph_original.type == "undirected" and DFS().is_acyclic(graph_original):
            path, exists = BFS().find_path(
                graph_original.source, graph_original.sink, graph_original.getNumNodes()
            )

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

        elif graph_original.type == "undirected":
            # convert original graph to graph with in and out vertecies for each vertex
            graph_split = Some.create_vertex_split_graph(graph_original)

            # Add a maxflow sink
            maxflow_sink = Node("maxflow_sink")
            graph_split.addNode(maxflow_sink)
            source_to_maxflow_sink = Edge(graph_split.source, maxflow_sink, 1)
            graph_split.addEdge(source_to_maxflow_sink)
            graph_split.getNode(graph_split.source.id).addOutgoingEdge(
                source_to_maxflow_sink
            )
            sink_to_maxflow_sink = Edge(graph_split.sink, maxflow_sink, 1)
            graph_split.addEdge(sink_to_maxflow_sink)
            graph_split.getNode(graph_split.sink.id).addOutgoingEdge(
                sink_to_maxflow_sink
            )

            path_has_been_found = False
            # try every red vertex as a starting point
            for vertex in graph_split.dictOfNodes.values():
                if path_has_been_found:
                    break
                if vertex.isRed:
                    max_flow = MaxFlow.fordFulkerson(
                        graph=graph_split, find_from=vertex, find_to=maxflow_sink
                    )
                    if max_flow == 2:
                        path_has_been_found = True

            if path_has_been_found:
                print("True")
            else:
                print("False")

        else:
            print("NP-hard")

    def create_vertex_split_graph(graph: Graph) -> Graph:
        # Create a new graph
        new_graph = Graph()

        # Mapping of old nodes to their split counterparts
        node_map = {}

        # Split the nodes
        for node_id, node in graph.dictOfNodes.items():
            # Create the in-node and out-node
            in_node = Node(
                f"{node_id}_in",
            )
            out_node = Node(
                f"{node_id}_out",
                source=node.isSource,
                sink=node.isSink,
                isRed=node.isRed,
            )

            # Add the split nodes to the new graph
            new_graph.addNode(in_node)
            new_graph.addNode(out_node)

            # Add an edge between the in-node and out-node
            split_edge = Edge(in_node, out_node, _capacity=1)
            new_graph.addEdge(split_edge)
            new_graph.getNode(in_node.id).addOutgoingEdge(split_edge)
            new_graph.getNode(out_node.id).addOutgoingEdge(split_edge)

            # Map the original node to its split counterparts
            node_map[node_id] = (in_node, out_node)

        # Add edges from the old graph to the new graph
        for edge_key, edge in graph.dictOfEdges.items():
            old_from_id = edge._from.id
            old_to_id = edge._to.id

            # Get the split nodes
            _, out_from_node = node_map[
                old_from_id
            ]  # outgoing edge comes from the out-node
            in_to_node, _ = node_map[old_to_id]  # incoming edge goes to the in-node

            # Create the new edge in the split graph
            new_edge = Edge(out_from_node, in_to_node, edge._capacity)
            new_graph.addEdge(new_edge)
            new_graph.getNode(out_from_node.id).addOutgoingEdge(new_edge)
            new_graph.getNode(in_to_node.id).addOutgoingEdge(new_edge)

        return new_graph
