class AlgBellmanFord:
    # инициализируем граф, матрицу, ее длину, вершину
    def __init__(self, graph):
        self._graph = graph
        self._matrix = self._graph.adjacency_matrix()
        self._matrix_len = len(self._matrix)

    # алгоритм Беллмана-Форда
    def distances(self, begin_vertex):
        if begin_vertex < 0 or begin_vertex > self._matrix_len:
            return -1

        costs = [1000000] * self._matrix_len  # массив расстояний до каждой из вершин
        costs[begin_vertex] = 0  # изначально расстояние до стартовой вершины = 0
        edges = self._graph.list_of_edges()

        # |V-1| раз повторяем, что если через ребро идти выгоднее
        for i in range(self._matrix_len - 1):
            for edge in edges:
                costs[edge[1]] = min(costs[edge[1]], costs[edge[0]] + edge[2])

        # последняя итерация нужна для проверки на цикл отрицательного веса
        # если даже на V-ой итерации мы можем сократить путь - цикл есть
        for edge in edges:
            if costs[edge[1]] > costs[edge[0]] + edge[2]:
                return -10

        return costs
