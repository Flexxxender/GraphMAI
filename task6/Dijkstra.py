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
        parents = [-1] * self.__matrix_len  # массив родителей для вершин
        visited = []  # массив посещенных в ходе алгоритма вершин
        count_visited = [0] * self.__matrix_len

        # изначально родителем стартовой вершины является она сама и расстояние до неё 0
        costs[self.__begin_vertex] = 0
        parents[self.__begin_vertex] = self.__begin_vertex
        node = self.__begin_vertex

        # пока не посетили все вершины
        while len(visited) != self.__matrix_len:
            # получаем соседей вершины
            neighbours = self.__graph.adjacency_list(self.__matrix, node)
            visited.append(node)

            # модификация Форда для алгоритма Дейкстры:
            # если в вершину вошли n раз - значит в графе есть цикл отрицательного веса
            count_visited[node] += 1
            if count_visited[node] == self.__matrix_len:
                return -10

            # если через текущую вершину node и ребро (node, neighbours[i)] быстрее дойти,
            # чем до вершины neighbours[i] не через вершину node - перезаписываем расстояние 
            # и добавляем node в качестве родителя для neighbours[i], ведь мы прошли через неё
            for i in range(len(neighbours)):
                new_cost = costs[node] + self.__matrix[node][neighbours[i]]

                if new_cost < costs[neighbours[i]]:
                    costs[neighbours[i]] = new_cost
                    parents[neighbours[i]] = node

                    # модификация Форда - если через вершину есть путь короче, 
                    # значит снимаем метку
                    if node in visited:
                        visited.remove(node)

            # далее выбираем новую с минимальным расстоянием из не посещенных
            node = self.__search_min_node(visited, costs)

        return costs

    # получение соседей с минимальным расстоянием из не посещенных
    def __search_min_node(self, visited, costs):
        min_cost = 1000000
        node = 0
        for i in range(self.__matrix_len):
            if i not in visited and costs[i] < min_cost:
                min_cost = costs[i]
                node = i

        return node