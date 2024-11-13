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
            print(f"Loop detected and skipped, from {_from} to {_to}, direction {_direction}.")
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
            print(f"Loop detected and skipped, from {_from} to {_to}, direction {_direction}.")
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
            print(f"Loop detected and skipped, from {_from} to {_to}, direction {_direction}.")
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
