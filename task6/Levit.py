class AlgLevit:
    # инициализируем граф, матрицу, ее длину, вершину
    def __init__(self, graph):
        self._graph = graph
        self._matrix = self._graph.adjacency_matrix()
        self._matrix_len = len(self._matrix)

    # алгоритм Левита
    def distances(self, begin_vertex):
        if begin_vertex < 0 or begin_vertex > self._matrix_len:
            return -1

        M0 = [i for i in range(self._matrix_len) if i != begin_vertex]  # необработанные вершины
        common_M1 = [begin_vertex]  # очередь на обработку
        urgent_M1 = []  # срочная очередь на обработку
        M2 = []  # предположительно обработанные вершины

        # массив расстояний до вершин, изначально до всех невозможно дойти,
        # а до стартовой расстояние 0
        costs = [1000000] * self._matrix_len
        costs[begin_vertex] = 0

        # пока очередь на обработку не пустая
        while len(common_M1) or len(urgent_M1):
            # выбираем первую вершину из очереди и смотрим ее соседей
            current_vertex = urgent_M1.pop(0) if len(urgent_M1) else common_M1.pop(0)
            neighbours = self._graph.adjacency_list(self._matrix, current_vertex)

            for neighbour in neighbours:
                # нашли ребра, инцидентные просматриваемой вершины
                edges = self._graph.list_of_edges(current_vertex)

                # если сосед необработан - обновляем расстояние, а соседа перемещаем в очередь на обработку
                if neighbour in M0:
                    costs[neighbour] = costs[current_vertex] + self.__find_edge(neighbour, edges)[2]
                    M0.remove(neighbour)
                    common_M1.append(neighbour)

                # если сосед в очереди на обработку - просто проверяем возможность сократить путь
                if neighbour in common_M1 or neighbour in urgent_M1:
                    if costs[neighbour] > costs[current_vertex] + self.__find_edge(neighbour, edges)[2]:
                        costs[neighbour] = costs[current_vertex] + self.__find_edge(neighbour, edges)[2]

                # если сосед предположительно обработан, то если через него можно сократить путь -
                # перемещаем в срочную очередь на обработку
                if neighbour in M2:
                    if costs[neighbour] > costs[current_vertex] + self.__find_edge(neighbour, edges)[2]:
                        costs[neighbour] = costs[current_vertex] + self.__find_edge(neighbour, edges)[2]
                        M2.remove(neighbour)
                        urgent_M1.append(neighbour)

            # перемещаем просматриваемую вершину в предположительно обработанные
            M2.append(current_vertex)

            # проверка на отрицательный цикл в графе
            for cost in costs:
                if cost < 0:
                    return -10

        return costs

    # нахождение ребер, которые ведут в вершину vertex
    @staticmethod
    def __find_edge(vertex, edges):
        for edge in edges:
            if edge[1] == vertex:
                return edge
        return 0
