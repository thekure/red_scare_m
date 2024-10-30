from queue import Queue
from sys import stdin


class Node:
    def __init__(self, id, source=False, sink=False, isRed=False):
        self.id = id
        self.outgoingEdges = set()
        self.isSource = source
        self.isSink = sink
        self.isRed = isRed

    def addOutgoingEdge(self, edge):
        self.outgoingEdges.add(edge)


class Edge:
    def __init__(self, _from: Node, _to: Node, _capacity=1):
        self._from = _from
        self._to = _to
        self._capacity = _capacity
        self._flow = 0

    def residualCapacityTo(self, node):
        if node.id is self._to.id:
            value = self._capacity - self._flow
        else:
            value = self._flow
        return value

    def addResidualFlowTo(self, flowValue, node):
        if node.id is self._to.id:
            self._flow += flowValue
        else:
            self._flow -= flowValue

    def getOther(self, node: Node):
        if node.id is self._from.id:
            return self._to
        else:
            return self._from

    def compareEdge(self, edge):
        if (
            self._from is edge._from
            and self._to is edge._to
            and self._capacity is edge._capacity
        ):
            return True
        else:
            return False

    def printEdge(self):
        print(
            self._from.id,
            "->",
            self._to.id,
            "FLOW:",
            self._flow,
            "CAPACITY:",
            self._capacity,
        )


class Graph:
    def __init__(self):
        self.dictOfNodes = {}
        self.dictOfEdges = {}
        self.source = None
        self.sink = None

    def addNode(self, node: Node):
        if node.isSink:
            self.sink = node
        if node.isSource:
            self.source = node

        if node.isSink and node.isSource:
            return "Same node can't be sink and source"

        self.dictOfNodes.update({node.id: node})

    def getEdge(self, edge: Edge):
        return self.dictOfEdges.get((edge._from, edge._to))

    def addEdge(self, edge: Edge):
        self.dictOfEdges.update({(edge._from, edge._to): edge})

    def getNode(self, id):
        return self.dictOfNodes.get(id)

    def findPathBFS(self, _from: Node, _to: Node, nodes):
        markedNodes = {}
        queue = Queue(maxsize=nodes)

        markedNodes[_from.id] = True

        queue.put(item=_from)  # and put it on the queue
        path = {}

        while not queue.empty():
            currentNode = queue.get()

            for edge in currentNode.outgoingEdges:
                otherNode = edge.getOther(currentNode)

                if edge.residualCapacityTo(otherNode) > 0 and not markedNodes.get(
                    otherNode.id
                ):
                    path[otherNode.id] = edge
                    markedNodes[otherNode.id] = True
                    queue.put(otherNode)

        return path, markedNodes.get(_to.id)

    # Ford fulkerson that uses BFS
    def findMaxFlowFF(self, nodes):
        maxFlow = 0

        path, isPath = self.findPathBFS(self.source, self.sink, nodes)

        while isPath:
            bottle = 9223372036854775807
            v = self.sink

            while v.id is not self.source.id:
                bottle = min(bottle, path.get(v.id).residualCapacityTo(v))
                v = path.get(v.id).getOther(v)

            v = self.sink
            while v.id is not self.source.id:
                path.get(v.id).addResidualFlowTo(bottle, v)
                v = path.get(v.id).getOther(v)

            maxFlow += bottle

            path, isPath = self.findPathBFS(self.source, self.sink, nodes)

        return maxFlow

    def printGraph(self):
        for node in self.dictOfNodes.values():
            print("----NODE----")
            print(f"ID: {node.id}")
            print(f"isSource: {node.isSource}")
            print(f"isSink: {node.isSink}")
            print(f"isRed: {node.isRed}")
            for edge in node.outgoingEdges:
                print(f"----OUTGOING EDGE from node {node.id}----")
                print("From: ", edge._from.id)
                print("To: ", edge._to.id)
            print()

        # for edge in self.dictOfEdges.values():
        #     print("----EDGES----")
        #     print("From:", edge._from.id)
        #     print("To:", edge._to.id)
        #     print("Capacity:", edge._capacity)
        #     print("Flow:", edge._flow)


# Graph, Node and Edge classes are implemented above.
# Below is an example of using it


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

    return num_nodes, graph


def solve():
    nodes, graph = create_graph()
    graph.printGraph()

    maxFlow = graph.findMaxFlowFF(nodes)
    print(f"maxflow: {maxFlow}")


solve()
