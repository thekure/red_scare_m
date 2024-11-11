from graphlib.graph import Node, Edge, Graph
from sys import stdin


def create_graph():
    num_nodes, num_edges, num_red = map(int, stdin.readline().split())
    source, sink = stdin.readline().split()

    graph = Graph()

    for _ in range(num_nodes):
        line = stdin.readline().split()
        id = line[0]
        isRed = False
        if len(line) > 1:
            isRed = True
        if id == source:
            graph.addNode(Node(id, source=True, isRed=isRed))
        elif id == sink:
            graph.addNode(Node(id, sink=True, isRed=isRed))
        else:
            graph.addNode(Node(id, isRed=isRed))

    for _ in range(num_edges):
        _from, _direction, _to = stdin.readline().split()
        isDirected = _direction == "->"

        edge1 = Edge(_from=graph.getNode(_from), _to=graph.getNode(_to))
        graph.addEdge(edge1)
        graph.getNode(_from).addOutgoingEdge(edge1)

        if not isDirected:
            edge2 = Edge(_from=graph.getNode(_to), _to=graph.getNode(_from))
            graph.addEdge(edge2)
            graph.getNode(_to).addOutgoingEdge(edge2)

    return graph

def create_weighted_graph_based_on_reds(negative_weight=False, weight_only_directed=False):
    num_nodes, num_edges, num_red = map(int, stdin.readline().split())
    source, sink = stdin.readline().split()

    graph = Graph()

    for _ in range(num_nodes):
        line = stdin.readline().split()
        id = line[0]
        isRed = False
        if len(line) > 1:
            isRed = True
        if id == source:
            graph.addNode(Node(id, source=True, isRed=isRed))
        elif id == sink:
            graph.addNode(Node(id, sink=True, isRed=isRed))
        else:
            graph.addNode(Node(id, isRed=isRed))

    for _ in range(num_edges):
        _from, _direction, _to = stdin.readline().split()
        isDirected = _direction == "->"
        unidrectedNoWeights = not isDirected and weight_only_directed

        graph.type = "directed" if isDirected else "undirected"

        # in case weight_only_directed is True => don't put weights on undirected graphs
        # otherwise, edge's weight is based only on the colour of the right node
        weight = 1 if graph.getNode(_to).isRed else 0
        weight *= -1 if negative_weight else 1

        edge1 = Edge(_from=graph.getNode(_from), _to=graph.getNode(_to)) if unidrectedNoWeights \
            else Edge(_from=graph.getNode(_from), _to=graph.getNode(_to), _capacity=weight)
        graph.addEdge(edge1)
        graph.getNode(_from).addOutgoingEdge(edge1)

        if not isDirected:
            weight = 1 if graph.getNode(_from).isRed else 0
            weight *= -1 if negative_weight else 1

            edge2 = Edge(_from=graph.getNode(_to), _to=graph.getNode(_from)) if unidrectedNoWeights \
                else Edge(_from=graph.getNode(_to), _to=graph.getNode(_from), _capacity=weight)
            graph.addEdge(edge2)
            graph.getNode(_to).addOutgoingEdge(edge2)

    return graph