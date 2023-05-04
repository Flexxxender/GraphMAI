class AlgPrima:
    def __init__(self, graph):
        self.__graph = graph
        self.__matrix = graph.associated_matrix()
        self.__matrix_len = len(self.__matrix)

    def spanning_tree(self):
        tree = []
        edges = self.__graph.list_of_edges()
        edges.sort(key=lambda edge: edge[2])
        vertices = [0] * self.__matrix_len
        vertices[0] = 1
        edge_adj = []

        while min(vertices) != max(vertices) and len(edges):
            for i in range(len(edges)):
                if (vertices[edges[i][0]] + vertices[edges[i][1]]) % 2:
                    edge_adj = edges[i]
                    break

            tree.append([edge_adj[0] + 1, edge_adj[1] + 1, edge_adj[2]])
            edges.remove(edge_adj)
            vertices[edge_adj[1]] = vertices[edge_adj[0]] = 1

        tree_weight = sum((tree[i][2] for i in range(len(tree))))
        return tree, tree_weight

