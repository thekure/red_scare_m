from queue import Queue
from abc import ABC, abstractmethod

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
