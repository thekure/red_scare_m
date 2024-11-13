from queue import Queue
from abc import ABC, abstractmethod
from sys import maxsize

from graphlib.graph import Node


class PathFinder(ABC):
    @abstractmethod
    def find_path(self, source, sink, graph_length=0):
        pass


class BFS(PathFinder):
    def find_path(self, _from: Node, _to: Node, nodes):
        markedNodes = {}
        queue = Queue(maxsize=nodes)

        markedNodes[_from.id] = True

        queue.put(item=_from)
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

    def find_alternating_path(self, _from: Node, _to: Node, nodes):
        markedNodes = {}
        queue = Queue(maxsize=nodes)

        markedNodes[_from.id] = True

        queue.put(item=_from)
        path = {}

        while not queue.empty():
            currentNode = queue.get()

            for edge in currentNode.outgoingEdges:
                otherNode = edge.getOther(currentNode)

                # if the node hasn't been visited and has the opposite color of the current node
                # only go down this road if the color of the next node is opposite than the current node
                if not markedNodes.get(otherNode.id) and (currentNode.isRed is not otherNode.isRed):
                    path[otherNode.id] = edge
                    markedNodes[otherNode.id] = True
                    queue.put(otherNode)

        return path, markedNodes.get(_to.id)


class DFS(PathFinder):
    def find_path(self, _from: Node, _to: Node, nodes):
        path, last_marked, markedNodes = self.find_path_helper(
            _from, _to, nodes, {}, {}
        )
        return path, last_marked

    def find_path_helper(
            self, _from: Node, _to: Node, nodes, path=None, markedNodes=None
    ):
        if path is None:
            path = {}
        if markedNodes is None:
            markedNodes = {}

        markedNodes[_from.id] = True

        for edge in _from.outgoingEdges:
            otherNode = edge.getOther(_from)

            if edge.residualCapacityTo(otherNode) > 0 and not markedNodes.get(
                    otherNode.id
            ):
                path[otherNode.id] = edge
                markedNodes[otherNode.id] = True

                if otherNode.id == _to.id:
                    return path, True, markedNodes

                path, last_marked, markedNodes = self.find_path_helper(
                    otherNode, _to, nodes, path, markedNodes
                )

                if last_marked:
                    return path, True, markedNodes

        return path, False, markedNodes

    def is_acyclic(self, graph):
        visited = {}
        for node in graph.dictOfNodes.values():
            if node.id not in visited:
                if not self.find_cycle_helper(node, None, visited):
                    return False
        return True

    def find_cycle_helper(self, node, parent, visited):
        visited[node.id] = True
        for edge in node.outgoingEdges:
            neighbor = edge.getOther(node)
            if neighbor.id not in visited:
                if not self.find_cycle_helper(neighbor, node, visited):
                    return False
            elif neighbor.id != parent.id:
                # Consider finding a cycle only if we find a visited node that isn't the parent
                return False
        return True


class BellmanFord(PathFinder):
    def find_path(self, graph):
        _from = graph.source
        dist = {node_id: maxsize for node_id in graph.dictOfNodes}
        dist[_from.id] = 0
        V = graph.getNumNodes()

        for i in range(V):
            for edge in graph.dictOfEdges.values():
                u = edge._from.id
                v = edge._to.id
                weight = edge._capacity

                if dist[u] != maxsize and dist[u] + weight < dist[v]:
                    if i == V - 1:
                        return -1  # negative cycle
                    dist[v] = dist[u] + weight

        dist = {node_id: abs(value) for node_id, value in dist.items()}
        return dist