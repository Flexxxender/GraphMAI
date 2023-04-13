import AbstractConnectivity


class DirectedGraph(AbstractConnectivity.GraphConnectivity):
    def __init__(self, graph):
        super().__init__(graph)
        self.__graph = graph
        self.__matrix = self.__graph.adjacency_matrix()
        self.__matrix_len = len(self.__matrix)

    def is_graph_weak_connected(self):
        return super().is_connected(self.associated_matrix())

    def count_weak_connected_components(self):
        return super().is_connected(self._adjacency_matrix)

    def associated_matrix(self):
        associated_matrix = self.__matrix

        for i in range(self.__matrix_len):
            for j in range(self.__matrix_len):
                if self.__graph.is_edge(i, j):
                    associated_matrix[j][i] = associated_matrix[i][j]

        return associated_matrix

    def kosaraju(self):
        transpose_matrix = self.transpose_matrix(self.__matrix)

    @staticmethod
    def transpose_matrix(matrix):
        new_matrix = [[0] * len(matrix) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix
