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

def create_normal_graph_and_without_red():
    num_nodes, num_edges, num_red = map(int, stdin.readline().split())
    source, sink = stdin.readline().split()

    graph = Graph()
    graph_without_red = Graph()

    for _ in range(num_nodes):
        line = stdin.readline().split()
        id = line[0]
        isRed = False
        if len(line) > 1:
            isRed = True
        if id == source:
            graph.addNode(Node(id, source=True, isRed=isRed))
            graph_without_red.addNode(Node(id, source=True, isRed=isRed))
        elif id == sink:
            graph.addNode(Node(id, sink=True, isRed=isRed))
            graph_without_red.addNode(Node(id, sink=True, isRed=isRed))
        elif isRed:
            graph.addNode(Node(id, isRed=isRed))
        else:
            graph.addNode(Node(id, isRed=isRed))
            graph_without_red.addNode(Node(id, isRed=isRed))

    for _ in range(num_edges):
        _from, _direction, _to = stdin.readline().split()
        isDirected = _direction == "->"
        noRedNodes = graph_without_red.getNode(_from) is not None and graph_without_red.getNode(_to) is not None

        if _to != _from:
            edge1 = Edge(_from=graph.getNode(_from), _to=graph.getNode(_to))
            graph.addEdge(edge1)
            graph.getNode(_from).addOutgoingEdge(edge1)

            if not isDirected:
                edge2 = Edge(_from=graph.getNode(_to), _to=graph.getNode(_from))
                graph.addEdge(edge2)
                graph.getNode(_to).addOutgoingEdge(edge2)

            if noRedNodes:
                edge1 = Edge(_from=graph_without_red.getNode(_from), _to=graph_without_red.getNode(_to))
                graph_without_red.addEdge(edge1)
                graph_without_red.getNode(_from).addOutgoingEdge(edge1)

                if not isDirected:
                    edge2 = Edge(_from=graph_without_red.getNode(_to), _to=graph_without_red.getNode(_from))
                    graph_without_red.addEdge(edge2)
                    graph_without_red.getNode(_to).addOutgoingEdge(edge2)

    return graph, graph_without_red