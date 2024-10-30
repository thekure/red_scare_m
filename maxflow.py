from queue import Queue
from sys import stdin


class Node:
    def __init__(self, id, source=False, sink=False):
        self.id = id
        self.adjacentEdges = set()
        self.isSource = source
        self.isSink = sink

    def addEdge(self, edge):
        self.adjacentEdges.add(edge)


class Edge:
    def __init__(self, _from: Node, _to: Node, _capacity):
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
        thisEdge = self.getEdge(edge)

        if thisEdge is None:
            self.dictOfEdges.update({(edge._from, edge._to): edge})
            return edge
        else:
            thisEdge._capacity += edge._capacity
            return thisEdge

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

            for edge in currentNode.adjacentEdges:
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
            print(node.id)
            print(node.isSource)
            print(node.isSink)
            for edge in node.adjacentEdges:
                print("----OUTGOING EDGE----")
                print("From:", edge._from.id)
                print("To:", edge._to.id)

        for edge in self.dictOfEdges.values():
            print("----EDGE----")
            print("From:", edge._from.id)
            print("To:", edge._to.id)
            print("Capacity:", edge._capacity)
            print("Flow:", edge._flow)


# Graph, Node and Edge classes are implemented above.
# Below is an example of using it


def create_graph():
    nodes, edges, source, sink = stdin.readline().split()

    nodes = int(nodes)
    edges = int(edges)
    source = int(source)
    sink = int(sink)

    graph = Graph()

    for node in range(nodes):
        if node == source:
            graph.addNode(Node(node, source=True))
        elif node == sink:
            graph.addNode(Node(node, sink=True))
        else:
            graph.addNode(Node(node))

    for _ in range(edges):
        _from, _to, _capacity = stdin.readline().split()
        _capacity = int(_capacity)
        _from = int(_from)
        _to = int(_to)

        newEdge = Edge(graph.getNode(_from), graph.getNode(_to), _capacity)

        updatedEdge = graph.addEdge(newEdge)

        graph.getNode(_from).addEdge(updatedEdge)
        graph.getNode(_to).addEdge(updatedEdge)

    return nodes, graph


def solve():
    nodes, graph = create_graph()

    maxFlow = graph.findMaxFlowFF(nodes)

    numberOfEdges = 0
    stringList = []

    for edge in graph.dictOfEdges.values():
        if edge._flow > 0:
            numberOfEdges += 1
            result = str(edge._from.id) + " " + str(edge._to.id) + " " + str(edge._flow)
            stringList.append(result)

    stringList.sort()
    print(nodes, maxFlow, numberOfEdges)
    for ele in stringList:
        print(ele)


solve()
