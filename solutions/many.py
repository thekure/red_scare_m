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
        print("?!")
    elif res == -1:
        print(-1) # no path
    else:
        print(res)


def many_directed_without_negative_cycles(graph):
    result = BellmanFord().find_path(graph)

    if result == -1: # negative weight cycle
        return None
    else:
        _to = graph.sink
        reds = result[_to.id]
        if reds == maxsize:
            return -1
        else:
            reds += 1 if graph.source.isRed else 0
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