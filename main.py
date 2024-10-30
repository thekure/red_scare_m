from graphlib.utils import create_graph

nodes, graph = create_graph()
graph.printGraph()

maxFlow = graph.findMaxFlowFF(nodes)
print(f"maxflow: {maxFlow}")
