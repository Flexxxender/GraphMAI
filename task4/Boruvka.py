class AlgBoruvka:
    def __init__(self, graph):
        self.__graph = graph
        self.__matrix = graph.associated_matrix()
        self.__matrix_len = len(self.__matrix)

    def spanning_tree(self):
        tree = []
        p, s = self.__init()
        components = self.__matrix_len
        edges = self.__graph.list_of_edges()
        min_edge = [-1 for i in range(self.__matrix_len)]
        tree_weight = 0

        while components != 1:
            for i in range(self.__matrix_len):
                min_edge[i] = -1

            for i, edge in enumerate(edges):
                if self.__root(edge[0], p) == self.__root(edge[1], p):
                    continue
                r_v = self.__root(edge[0], p)
                if min_edge[r_v] == -1 or edge[2] < edges[min_edge[r_v]][2]:
                    min_edge[r_v] = i
                r_u = self.__root(edge[1], p)
                if min_edge[r_u] == -1 or edge[2] < edges[min_edge[r_u]][2]:
                    min_edge[r_u] = i

            for i in range(self.__matrix_len):
                if min_edge[i] != -1 and self.__union(edges[min_edge[i]][0], edges[min_edge[i]][1], p, s):
                    tree.append([edges[min_edge[i]][0] + 1, edges[min_edge[i]][1] + 1, edges[min_edge[i]][2]])
                    tree_weight += edges[min_edge[i]][2]
                    components -= 1

        return tree, tree_weight

    def __init(self):
        p = [i for i in range(self.__matrix_len)]
        s = [1 for i in range(self.__matrix_len)]
        return p, s

    def __root(self, vertice: int, parent: list) -> int:
        if parent[vertice] != vertice:
            parent[vertice] = self.__root(parent[vertice], parent)
        return parent[vertice]

    def __union(self, aa, bb, parent, size):
        a = self.__root(aa, parent)
        b = self.__root(bb, parent)
        if a == b:
            return False
        elif size[a] > size[b]:
            parent[b] = a
            size[a] += size[b]
        else:
            parent[a] = b
            size[b] += size[a]
        return True
