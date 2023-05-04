class AlgKruskal:
    def __init__(self, graph):
        self.__graph = graph
        self.__matrix = graph.associated_matrix()
        self.__matrix_len = len(self.__matrix)

    # def spanning_tree(self):
    #     start = time.time()
    #     tree = []
    #     edges = self.__graph.list_of_edges()
    #     vertices_belongs = [int(i) for i in range(self.__matrix_len)]
    #
    #     edges.sort(key=lambda edge: edge[2])
    #
    #     while len(edges) and (min(vertices_belongs) != max(vertices_belongs)):
    #         if vertices_belongs[edges[0][0]] != vertices_belongs[edges[0][1]]:
    #
    #             tree.append([edges[0][0] + 1, edges[0][1] + 1, edges[0][2]])
    #
    #             for i in range(len(vertices_belongs)):
    #                 if vertices_belongs[i] == vertices_belongs[edges[0][0]] and i != edges[0][0]:
    #                     vertices_belongs[i] = vertices_belongs[edges[0][1]]
    #             vertices_belongs[edges[0][0]] = vertices_belongs[edges[0][1]]
    #
    #         edges.pop(0)
    #
    #     tree_weight = sum((tree[i][2] for i in range(len(tree))))
    #
    #     end = time.time() - start
    #     print(end)
    #     print(tree_weight)
    #
    #     return tree, tree_weight

    def spanning_tree(self):
        p, s = self.__init()
        edges = self.__graph.list_of_edges()
        edges.sort(key=lambda edge: edge[2])
        tree = []

        for edge in edges:
            if self.__root(edge[0], p) != self.__root(edge[1], p):
                tree.append(edge)
                self.__union(edge[0], edge[1], p, s)

        tree_weight = sum((tree[i][2] for i in range(len(tree))))
        return tree, tree_weight

    def __init(self):
        p = [i for i in range(self.__matrix_len)]
        s = [1 for i in range(self.__matrix_len)]
        return p, s

    def __root(self, vertice: int, parent: list) -> int:
        if parent[vertice] != vertice:
            parent[vertice] = self.__root(parent[vertice], parent)
        return parent[vertice]

    def __union(self, aa, bb, parent, s):
        a = self.__root(aa, parent)
        b = self.__root(bb, parent)
        parent[a] = b