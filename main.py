from algorithms.pathfinding import DFS
from graphlib.utils import create_graph
from algorithms.maxflow import MaxFlow

graph = create_graph()
graph.printGraph()

maxFlow = MaxFlow.fordFulkerson(graph)
# maxFlow = MaxFlow.fordFulkerson(graph, DFS())

print(f"maxflow: {maxFlow}")
