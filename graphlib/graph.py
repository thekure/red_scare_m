class Node:
    def __init__(self, id, source=False, sink=False, isRed=False):
        self.id = id
        self.outgoingEdges = set()
        self.isSource = source
        self.isSink = sink
        self.isRed = isRed

    def addOutgoingEdge(self, edge):
        self.outgoingEdges.add(edge)
    
    def printNode(self):
        print(f"ID: {self.id} isSource: {self.isSource} isSink: {self.isSink} isRed: {self.isRed}")


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
        self.type = None

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

    def getNumNodes(self):
        return len(self.dictOfNodes.keys())

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
                print("Capacity: ", edge._capacity)
            print()
