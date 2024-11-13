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

        if (_from == _to):  # Check for loops.
            continue

        edge1 = Edge(_from=graph.getNode(_from), _to=graph.getNode(_to))
        graph.addEdge(edge1)
        graph.getNode(_from).addOutgoingEdge(edge1)

        if not isDirected:
            edge2 = Edge(_from=graph.getNode(_to), _to=graph.getNode(_from))
            graph.addEdge(edge2)
            graph.getNode(_to).addOutgoingEdge(edge2)

    return graph


def create_graph_without_red():
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
        elif not isRed:
            graph.addNode(Node(id, isRed=isRed))

    for _ in range(num_edges):
        _from, _direction, _to = stdin.readline().split()
        isDirected = _direction == "->"

        if (_from == _to):  # Check for loops.
            continue

        noRedNodes = graph.getNode(_from) is not None and graph.getNode(_to) is not None

        if noRedNodes:
            edge1 = Edge(_from=graph.getNode(_from), _to=graph.getNode(_to))
            graph.addEdge(edge1)
            graph.getNode(_from).addOutgoingEdge(edge1)

            if not isDirected:
                edge2 = Edge(_from=graph.getNode(_to), _to=graph.getNode(_from))
                graph.addEdge(edge2)
                graph.getNode(_to).addOutgoingEdge(edge2)

    return graph


def create_graphs_without_sink_and_without_source():
    num_nodes, num_edges, num_red = map(int, stdin.readline().split())
    source, sink = stdin.readline().split()

    graph_without_sink = Graph()
    graph_without_source = Graph()

    for _ in range(num_nodes):
        line = stdin.readline().split()
        id = line[0]
        isRed = False
        if len(line) > 1:
            isRed = True
        if id == source:
            graph_without_sink.addNode(Node(id, source=True, isRed=isRed))
        elif id == sink:
            graph_without_source.addNode(Node(id, sink=True, isRed=isRed))
        else:
            graph_without_sink.addNode(Node(id, isRed=isRed))
            graph_without_source.addNode(Node(id, isRed=isRed))

    for _ in range(num_edges):
        _from, _direction, _to = stdin.readline().split()
        isDirected = _direction == "->"

        if (_from == _to):  # Check for loops.
            continue

        if _from != sink and _to != sink:
            edge1 = Edge(_from=graph_without_sink.getNode(_from), _to=graph_without_sink.getNode(_to))
            graph_without_sink.addEdge(edge1)
            graph_without_sink.getNode(_from).addOutgoingEdge(edge1)

            if not isDirected:
                edge2 = Edge(_from=graph_without_sink.getNode(_to), _to=graph_without_sink.getNode(_from))
                graph_without_sink.addEdge(edge2)
                graph_without_sink.getNode(_to).addOutgoingEdge(edge2)

        if _from != source and _to != source:
            edge1 = Edge(_from=graph_without_source.getNode(_from), _to=graph_without_source.getNode(_to))
            graph_without_source.addEdge(edge1)
            graph_without_source.getNode(_from).addOutgoingEdge(edge1)

            if not isDirected:
                edge2 = Edge(_from=graph_without_source.getNode(_to), _to=graph_without_source.getNode(_from))
                graph_without_source.addEdge(edge2)
                graph_without_source.getNode(_to).addOutgoingEdge(edge2)

    return graph_without_sink, graph_without_source

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

        if (_from == _to):  # Check for loops.
            continue

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

        if _to != _from: # avoid loops
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