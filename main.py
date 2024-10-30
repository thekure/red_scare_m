from algorithms.pathfinding import DFS, BFS
from graphlib.utils import create_graph, create_none_graph
from algorithms.maxflow import MaxFlow, NoneOrSome

def solve_none():
    graph = create_none_graph()
    graph.printGraph()
    NoneOrSome.none(graph)
    
solve_none()