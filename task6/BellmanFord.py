class AlgBellmanFord:
    # инициализируем граф, матрицу, ее длину, начальную и конечную вершины,
    # а также результат алгоритма - расстояние и путь между вершинами
    def __init__(self, graph, begin_vertex):
        self.__graph = graph
        self.__matrix = self.__graph.adjacency_matrix()
        self.__matrix_len = len(self.__matrix)
        self.__begin_vertex = begin_vertex

        self.distance = self.__bellman_ford()

    # алгоритм Беллмана-Форда
    def __bellman_ford(self):
        costs = [1000000] * self.__matrix_len  # массив расстояний до каждой из вершин
        costs[self.__begin_vertex] = 0 # изначально расстояние до стартовой вершины = 0
        edges = self.__graph.list_of_edges()

        # |V-1| раз повторяем, что если через ребро идти выгоднее
        for i in range(self.__matrix_len - 1):
            for edge in edges:
                costs[edge[1]] = min(costs[edge[1]], costs[edge[0]] + edge[2])

        # последняя итерация нужна для проверки на цикл отрицательного веса
        # если даже на V-ой итерации мы можем сократить путь - цикл есть
        for edge in edges:
            if costs[edge[1]] > costs[edge[0]] + edge[2]:
                return -10
        
        return costs

        