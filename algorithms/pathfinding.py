from collections import deque
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


class BinaryBFS(PathFinder):
    def find_path(self, graph):
        # use double-ended queue:
        # add node to the front of the deque if its weight is 0
        # add node to the back of the deque if its weight is 1

        _from = graph.source
        _to = graph.sink

        dist = {node_id: maxsize for node_id in graph.dictOfNodes}
        dist[_from.id] = 0

        queue = deque()
        queue.append(_from)

        while queue:
            current_node = queue.popleft()

            for edge in current_node.outgoingEdges:
                other_node = edge.getOther(current_node)

                new_distance = dist[current_node.id] + edge._capacity
                if dist[other_node.id] > new_distance:
                    dist[other_node.id] = new_distance

                    if edge._capacity == 0:
                        queue.appendleft(other_node)
                    else:
                        queue.append(other_node)

        return dist[_to.id]


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