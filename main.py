from graphlib.utils import create_graph, create_graph_without_red, create_weighted_graph_based_on_reds, \
    create_normal_graph_and_without_red, create_graphs_without_sink_and_without_source
from solutions import many
from solutions.alternating import Alternating
from solutions.none import _None
from solutions.few import Few
from solutions.some import Some
from solutions.some_using_none import Some_Using_None


def solve_alternating():
    g = create_graph()
    Alternating.solve(g)

def solve_few():
    g = create_weighted_graph_based_on_reds()
    Few.solve(g)

def solve_none():
    g = create_graph_without_red()
    _None.solve(g)

def solve_some_using_none():
    g, g_without_red = create_normal_graph_and_without_red()
    Some_Using_None.solve(g, g_without_red)

def solve_some_idea():
    g, g_without_sink, g_without_source = create_graphs_without_sink_and_without_source()
    Some.solve(g, g_without_sink, g_without_source)

def solve_many():
    many.solve()


# uncomment/comment to enable/disable which problem to solve

# NONE ---- FEW ---- ALTERNATING
#solve_none()
#solve_few()
#solve_alternating()

# SOME
solve_some_idea()
#solve_some_using_none()

# MANY
#solve_many()



