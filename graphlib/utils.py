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

        if(_from == _to): # Check for loops.
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
        else:
            graph.addNode(Node(id, isRed=isRed))

    for _ in range(num_edges):
        _from, _direction, _to = stdin.readline().split()
        isDirected = _direction == "->"

        if (_from == _to):  # Check for loops.
            print(f"Loop detected and skipped, from {_from} to {_to}, direction {_direction}.")
            continue

        from_node = graph.dictOfNodes.get(_from)
        to_node = graph.dictOfNodes.get(_to)

        """ I'm unsure about what should happen when the sink or source is red """
        if (not from_node.isRed and not to_node.isRed) or (
            from_node.isSource and to_node.isSink  # idk about this...
        ):
            edge1 = Edge(_from=graph.getNode(_from), _to=graph.getNode(_to))
            graph.addEdge(edge1)
            graph.getNode(_from).addOutgoingEdge(edge1)

            if not isDirected:
                edge2 = Edge(_from=graph.getNode(_to), _to=graph.getNode(_from))
                graph.addEdge(edge2)
                graph.getNode(_to).addOutgoingEdge(edge2)

    return graph
