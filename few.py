from graphlib.utils import create_weighted_graph_based_on_reds
from solutions.few import Few

def solve_few():
    g = create_weighted_graph_based_on_reds()
    Few.solve(g)

solve_few()