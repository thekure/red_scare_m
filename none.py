from graphlib.utils import create_graph, create_graph_without_red, create_weighted_graph_based_on_reds, \
    create_normal_graph_and_without_red, create_graphs_without_sink_and_without_source
from solutions import many
from solutions.alternating import Alternating
from solutions.none import _None
from solutions.few import Few
from solutions.some import Some
from solutions.some_using_none import Some_Using_None

def solve_none():
    g = create_graph_without_red()
    _None.solve(g)

solve_none()