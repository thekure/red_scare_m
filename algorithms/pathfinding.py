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
    
    """ find all paths in a graph using DFS
        source code: @chatGPT

        returns: all_paths {}
            a dictionary mapping from has_red to path

        i.e. all_paths will have max 2 paths (one True and one False)
    """
    def find_all_paths(self, _from: Node, _to: Node):
        all_paths = {}  # To store all found paths
        path = []  # Current path being explored
        visited = set()  # Set to keep track of visited nodes on the current path

        def dfs_all_paths(currentNode, has_red):
            if currentNode.isRed:
                has_red = True
            # Add current node to path and mark it as visited
            path.append(currentNode)
            visited.add(currentNode.id)

            # If we reach the target node, add the current path to all_paths
            if currentNode == _to:
                all_paths[has_red] = list(path) # Make a copy of the path
            else:
                # Explore all outgoing edges from the current node
                for edge in currentNode.outgoingEdges:
                    otherNode = edge.getOther(currentNode)

                    # Only proceed if the edge has residual capacity and the node has not been visited
                    if edge.residualCapacityTo(otherNode) > 0 and otherNode.id not in visited:
                        dfs_all_paths(otherNode, has_red)  # Recursive call to continue path

            # Backtrack: remove the current node from path and visited set
            path.pop()
            visited.remove(currentNode.id)

        # Start the DFS from the source node
        dfs_all_paths(_from, has_red=False)
        return all_paths
        
