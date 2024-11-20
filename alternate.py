from graphlib.utils import create_graph
from solutions.alternating import Alternating

def solve_alternating():
    g = create_graph()
    Alternating.solve(g)

solve_alternating()