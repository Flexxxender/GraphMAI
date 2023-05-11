class AlgDijkstra:
    # инициализируем граф, матрицу, ее длину, начальную и конечную вершины,
    # а также результат алгоритма - расстояние и путь между вершинами
    def __init__(self, graph, begin_vertex):
        self.__graph = graph
        self.__matrix = self.__graph.adjacency_matrix()
        self.__matrix_len = len(self.__matrix)
        self.__begin_vertex = begin_vertex

        self.distance = self.__dijkstra()

    # алгоритм Дейкстры
    def __dijkstra(self):
        costs = [1000000] * self.__matrix_len  # массив расстояний до каждой из вершин
        visited = [False] * self.__matrix_len  # массив посещенных в ходе алгоритма вершин
        true_visited = 0  # кол-во посещенных вершин
        count_visited = [0] * self.__matrix_len  # массив, содержащий количество посещений вершин

        # изначально расстояние до стартовой вершины 0
        costs[self.__begin_vertex] = 0

        # пока не посетили все вершины
        while true_visited != self.__matrix_len:
            # выбираем вершину с минимальным расстоянием из не посещенных
            node = self.__search_min_node(visited, costs)
            if node == -1:
                break

            visited[node] = True
            true_visited += 1
            count_visited[node] += 1
            # получаем соседей вершины
            neighbours = self.__graph.adjacency_list(self.__matrix, node)
            # если через текущую вершину node и ребро (node, neighbours[i)] быстрее дойти,
            # чем до вершины neighbours[i] не через вершину node - перезаписываем расстояние
            for neighbour in neighbours:
                new_cost = costs[node] + self.__matrix[node][neighbour]
                if new_cost < costs[neighbour]:
                    costs[neighbour] = new_cost
                    # модификация Форда - если через вершину есть путь короче, 
                    # значит снимаем метку
                    if visited[neighbour]:
                        visited[neighbour] = False
                        true_visited -= 1

            # модификация Форда для алгоритма Дейкстры:
            # если в вершину вошли n раз - значит в графе есть цикл отрицательного веса
            for count in count_visited:
                if count == self.__matrix_len:
                    return -10

        return costs

    # получение соседей с минимальным расстоянием из не посещенных
    def __search_min_node(self, visited, costs):
        min_cost = 1000001
        node = -1
        for i in range(self.__matrix_len):
            if not visited[i] and costs[i] < min_cost:
                min_cost = costs[i]
                node = i

        return node
