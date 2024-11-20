from graphlib.utils import (
    create_graphs_without_sink_and_without_source,
)
from solutions.some import Some

def solve_some():
    (
        graph_original,
        g_without_sink,
        g_without_source,
    ) = create_graphs_without_sink_and_without_source()
    Some.solve(
        graph_original,
        g_without_sink,
        g_without_source,
    )

solve_some()