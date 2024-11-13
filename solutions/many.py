from sys import maxsize

from algorithms.pathfinding import BellmanFord, BFS, DFS
from graphlib.utils import create_weighted_graph_based_on_reds

def solve():
    graph = create_weighted_graph_based_on_reds(negative_weight=True, weight_only_directed=True)
    res = None

    # Directed Graph without negative weight cycle => use BellmanFord with negative weights
    if graph.type == "directed":
        res = many_directed_without_negative_cycles(graph)
    # Undirected Acyclic Graph (~ tree) => one or no path at all between source and sink => use BFS
    elif graph.type == "undirected" and DFS().is_acyclic(graph):
        res = many_undirected_acyclic_graph(graph)

    if res is None:
        print("NP-hard")
    elif res == -1:
        print("Many -> No path between source and sink")
    else:
        print(f"Many -> Maximum number of reds from {graph.source.id} to {graph.sink.id} is: {res}")


def many_directed_without_negative_cycles(graph):
    reds = 1 if graph.source.isRed else 0
    res = BellmanFord().find_path(graph)

    if res == -1: # negative weight cycle
        return None
    elif reds == maxsize:
        return -1
    else:
        _to = graph.sink
        reds += res[_to.id]
        return reds

def many_undirected_acyclic_graph(graph):
    reds = 1 if graph.source.isRed else 0
    path, exists = BFS().find_path(graph.source, graph.sink, graph.getNumNodes())

    if exists:
        current_node = graph.sink
        while current_node != graph.source:
            reds += 1 if current_node.isRed else 0
            edge = path.get(current_node.id)
            current_node = edge.getOther(current_node)
        return reds
    else:
        return -1