class AlgKruskal:
    def __init__(self, graph):
        self.__graph = graph
        self.__matrix = graph.associated_matrix()
        self.__matrix_len = len(self.__matrix)

        #self.spanning_tree = self.__spanning_tree()

    def spanning_tree(self):
        tree = []
        edges = self.__graph.list_of_edges()
        vertices_belongs = [int(i) for i in range(self.__matrix_len)]

        edges.sort(key=lambda edge: edge[2])

        while len(edges) and (min(vertices_belongs) != max(vertices_belongs)):
            if vertices_belongs[edges[0][0]] != vertices_belongs[edges[0][1]]:

                tree.append([edges[0][0] + 1, edges[0][1] + 1, edges[0][2]])

                for i in range(len(vertices_belongs)):
                    if vertices_belongs[i] == vertices_belongs[edges[0][0]] and i != edges[0][0]:
                        vertices_belongs[i] = vertices_belongs[edges[0][1]]
                vertices_belongs[edges[0][0]] = vertices_belongs[edges[0][1]]

            edges.pop(0)

        tree_weight = sum((tree[i][2] for i in range(len(tree))))

        return tree, tree_weight
