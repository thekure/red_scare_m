from graphlib.graph import Graph
from algorithms.pathfinding import BFS


class MaxFlow:

    """Ford fulkerson that uses BFS as default"""

    def fordFulkerson(graph: Graph, pathfinder=BFS()):
        maxFlow = 0
        num_nodes = graph.getNumNodes()

        path, isPath = pathfinder.find_path(graph.source, graph.sink, num_nodes)

        while isPath:
            bottle = 9223372036854775807
            v = graph.sink

            while v.id is not graph.source.id:
                bottle = min(bottle, path.get(v.id).residualCapacityTo(v))
                v = path.get(v.id).getOther(v)

            v = graph.sink
            while v.id is not graph.source.id:
                path.get(v.id).addResidualFlowTo(bottle, v)
                v = path.get(v.id).getOther(v)

            maxFlow += bottle

            path, isPath = pathfinder.find_path(graph.source, graph.sink, num_nodes)

        return maxFlow
    

class NoneOrSome:
    def none(graph: Graph, pathfinder=BFS()):
        num_nodes = graph.getNumNodes()
        path, isPath = pathfinder.find_path(graph.source, graph.sink, num_nodes)

        if not isPath:
            # if there is no path from s to t
            print(f"-1")
        else:
            # otherwise a path exists and we need to find the length of it
            v = graph.sink
            length = 0
            while v.id is not graph.source.id:
                length += 1
                v = path.get(v.id).getOther(v)
            print(f"{length}")

    def some(graph: Graph):
        # create the the memory table
        print(f"numnodes: {graph.getNumNodes()}")
        memory = [[False for i in range(graph.getNumNodes())] for j in range(graph.getNumNodes())]
        for row in memory:
            print(row)

        # fill in the memory table
        for node in graph.dictOfNodes.values():
            node.printNode()
            for edge in node.outgoingEdges:
                print(f"memory[{int(node.id)}][{int(edge._to.id)}]")
                memory[int(node.id)][int(edge._to.id)] = edge._to.isRed or edge._from.isRed
                
            
            print()
            
        for row in memory:
            print(row)
        
        # # start from the sink id
        node = int(graph.sink.id)

        # this seems hacky, should we do something else?
        possiblePath = -1
        path = False
        print(f"graphs source: {graph.source.id}")
        print(f"initial node: {node}")
        
        while int(node) != int(graph.source.id):
            if possiblePath + 1 == len(memory[0]):
                path = False
                break

            possiblePath += 1
            print(f"node: [{node}][{possiblePath}]")
            
            # there is a possible path
            if memory[node][possiblePath]:
                print(f"there is a possible path [{node}][{possiblePath}]")
                node = possiblePath
                path = True
                possiblePath = -1

        print(f"path found {path}")
        return 
        
