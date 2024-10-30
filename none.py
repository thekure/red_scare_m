from algorithms.pathfinding import BFS
from graphlib.utils import create_graph_without_red

graph = create_graph_without_red()
# graph.printGraph()

path, hasPathBeenFound = BFS().find_path(graph.source, graph.sink, graph.getNumNodes())

v = graph.sink
length = 0
path_lst = [v.id]

while v.id is not graph.source.id:
    other_v = path.get(v.id)
    if other_v is None:
        break
    else:
        v = path.get(v.id).getOther(v)
        length += 1
        path_lst.append(v.id)

if hasPathBeenFound:
    print(f"length of shortest path: {length}")
else:
    print(f"no path: {-1}")


# print(f"has path been found: {hasPathBeenFound}")

# for i in reversed(path_lst):
#     print(i)
