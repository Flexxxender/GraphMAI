from task2 import AbstractConnectivity


class DirectedGraph(AbstractConnectivity.GraphConnectivity):
    def __init__(self, graph):
        super().__init__(graph)
        self.__graph = graph
        self.__matrix = self.__graph.adjacency_matrix()
        self.__matrix_len = len(self.__matrix)

    def is_graph_weak_connected(self):
        return super().is_connected(self.associated_matrix())

    def count_weak_connected_components(self):
        return super().count_connected_components(self.associated_matrix())

    def associated_matrix(self):
        associated_matrix = self.__graph.adjacency_matrix()

        for i in range(self.__matrix_len):
            for j in range(self.__matrix_len):
                if self.__graph.is_edge(i, j):
                    associated_matrix[j][i] = associated_matrix[i][j]

        return associated_matrix

    def kosaraju(self):
        components = []
        count_components = 0
        transpose_matrix = self.transpose_matrix(self.__matrix)

        counters = [0] * self.__matrix_len
        vertices = [i for i in range(self.__matrix_len)]
        counter = [0]

        while len(vertices):
            dfs_result = super().DFS(vertices[0], counter,
                                     counters, self.__matrix)
            for vertex in dfs_result:
                vertices.pop(vertices.index(vertex))

        counters_copy = [0] * self.__matrix_len
        vertices = [i for i in range(self.__matrix_len)]
        counter = [0]

        while len(vertices):
            component = super().DFS(counters.index(max(counters)), counter, counters_copy, transpose_matrix)

            count_components += 1
            components.append(component)
            for vertex in component:
                vertices.pop(vertices.index(vertex))
                counters[vertex] = 0

        return count_components, components

    @staticmethod
    def transpose_matrix(matrix):
        new_matrix = [[0] * len(matrix) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix
