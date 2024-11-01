from algorithms.pathfinding import DFS, BFS
from graphlib.utils import create_graph, create_none_graph
from algorithms.algorithms import MaxFlow, NoneOrSome


def solve_none():
    graph = create_none_graph()
    NoneOrSome.none(graph)

def solve_some():
    graph = create_graph()
    NoneOrSome.some(graph)
    
#solve_none()
solve_some()