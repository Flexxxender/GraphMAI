from task2 import AbstractConnectivity


class UndirectedGraph(AbstractConnectivity.GraphConnectivity):
    def __init__(self, graph):
        super().__init__(graph)

    def is_graph_connected(self):
        return super().is_connected(self._adjacency_matrix)

    def count_graph_connected_components(self):
        return super().count_connected_components(self._adjacency_matrix)