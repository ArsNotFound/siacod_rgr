from model import Graph


def warshall(graph: Graph) -> Graph:
    w = graph.matrix.copy()
    n = len(w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w[i][j] = w[i][j] or (w[i][k] and w[k][j])

    return Graph(w, graph.header)
