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
