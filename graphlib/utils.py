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

""" Make a graph, G', which is a copy of the graph G, but there are no edges connecting to or from the colored nodes.
    Except for the source and sink nodes, since we don't care about their color. """
def create_none_graph():
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
        
        # only add the edge if the two nodes are not red
        # don't care about the color of sink and source
        if (edge1._from.isSource and not edge1._to.isRed) or (edge1._to.isSink and not edge1._from.isRed) or (not edge1._from.isRed and not edge1._to.isRed):
            graph.addEdge(edge1)
            graph.getNode(_from).addOutgoingEdge(edge1)

        if not isDirected:
            edge2 = Edge(_from=graph.getNode(_to), _to=graph.getNode(_from))
            # only add the edge if the two nodes are not red
            # don't care about the color of sink and source
            if (edge1._from.isSource and not edge1._to.isRed) or (edge1._to.isSink and not edge1._from.isRed) or (not edge1._from.isRed and not edge1._to.isRed):
                graph.addEdge(edge2)
                graph.getNode(_to).addOutgoingEdge(edge2)

    return graph


