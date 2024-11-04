from algorithms.pathfinding import DFS, BFS
from graphlib.utils import create_graph, create_none_graph
from algorithms.algorithms import MaxFlow, NoneOrSome, Alternating


def solve_none():
    graph = create_none_graph()
    NoneOrSome.none(graph)

def solve_some():
    graph = create_graph()
    NoneOrSome.some(graph)

def solve_alternating():
    graph = create_graph()
    Alternating.alternating(graph)

    
#solve_none()
#solve_some()
solve_alternating()