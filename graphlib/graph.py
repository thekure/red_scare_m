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
        print(
            f"ID: {self.id} isSource: {self.isSource} isSink: {self.isSink} isRed: {self.isRed}"
        )


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

    def removeEdge(self, edge: Edge):
        self.dictOfEdges.pop((edge._from, edge._to))

    def getNode(self, id):
        return self.dictOfNodes.get(id)

    def getNumNodes(self):
        return len(self.dictOfNodes.keys())

    # This method was written with the help of chatGPT
    def isCyclic(self):
        """
        Check if the graph contains a cycle.
        Returns True if the graph is cyclic, False otherwise.
        Handles both directed and undirected graphs.
        """
        visited = set()

        def dfs_directed(node, recStack):
            # Mark the current node as visited and add to recursion stack
            visited.add(node)
            recStack.add(node)

            # Traverse all outgoing edges
            for edge in node.outgoingEdges:
                neighbor = edge._to
                if neighbor not in visited:
                    if dfs_directed(neighbor, recStack):
                        return True
                elif neighbor in recStack:
                    # A cycle is detected
                    return True

            # Remove the node from recursion stack after exploration
            recStack.remove(node)
            return False

        def dfs_undirected(node, parent):
            # Mark the current node as visited
            visited.add(node)

            # Traverse all outgoing edges
            for edge in node.outgoingEdges:
                neighbor = edge._to
                if neighbor not in visited:
                    if dfs_undirected(neighbor, node):
                        return True
                elif neighbor != parent:
                    # A cycle is detected (ignoring the trivial parent backtrack)
                    return True

            return False

        # Choose the correct DFS method based on the graph type
        if self.type == "directed":
            for node in self.dictOfNodes.values():
                if node not in visited:
                    if dfs_directed(node, set()):
                        return True
        elif self.type == "undirected":
            for node in self.dictOfNodes.values():
                if node not in visited:
                    if dfs_undirected(node, None):
                        return True

        return False

    # For debugging
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
                print("Flow: ", edge._flow)
            print()
