from graphlib.utils import create_graph
from algorithms.maxflow import MaxFlow

graph = create_graph()
graph.printGraph()

maxFlow = MaxFlow.fordFulkerson(graph)
print(f"maxflow: {maxFlow}")
