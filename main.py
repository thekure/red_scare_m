from graphlib.utils import create_graph

graph = create_graph()
graph.printGraph()

maxFlow = graph.findMaxFlowFF(graph.getNumNodes())
print(f"maxflow: {maxFlow}")
