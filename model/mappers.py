import graph
from . import graph as model


__all__ = ("graph_to_model",)


def graph_to_model(g: graph.Graph) -> model.Graph:
    nodes = list(g.nodes)
    nodes.sort(key=lambda n: n.value)

    header = list(map(lambda n: n.value, nodes))

    matrix = [[0 for _ in range(len(g.nodes))] for _ in range(len(g.nodes))]
    for e in g.edges:
        i = nodes.index(e.src)
        j = nodes.index(e.dest)
        matrix[i][j] = 1
        matrix[j][i] = 1

    return model.Graph(matrix, header)
