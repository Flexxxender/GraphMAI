class GraphDijkstra:
    # инициализируем граф, матрицу, ее длину, начальную и конечную вершины,
    # а также результат алгоритма - расстояние и путь между вершинами
    def __init__(self, graph, begin_vertex, end_vertex):
        self.__graph = graph
        self.__matrix = self.__graph.adjacency_matrix()
        self.__matrix_len = len(self.__matrix)
        self.__begin_vertex = begin_vertex
        self.__end_vertex = end_vertex

        self.distance, self.route = self.__dijkstra()

    # алгоритм Дейкстры
    def __dijkstra(self):
        if self.__begin_vertex >= self.__matrix_len or self.__end_vertex >= self.__matrix_len or \
                self.__begin_vertex < 0 or self.__end_vertex < 0:
            return -2, -2

        costs = [1000000] * self.__matrix_len  # массив расстояний до каждой из вершин
        parents = [-1] * self.__matrix_len  # массив родителей для вершин
        visited = []  # массив посещенных в ходе алгоритма вершин

        # изначально родителем стартовой вершины является она сама и расстояние до неё 0
        costs[self.__begin_vertex] = 0
        parents[self.__begin_vertex] = self.__begin_vertex
        node = self.__begin_vertex

        # пока не посетили все вершины
        while len(visited) != self.__matrix_len:
            # получаем соседей вершины
            neighbours = self.__graph.adjacency_list(self.__matrix, node)

            # если через текущую вершину node и ребро (node, neighbours[i)] быстрее дойти,
            # чем до вершины neighbours[i] не через вершину node - перезаписываем расстояние 
            # и добавляем node в качестве родителя для neighbours[i], ведь мы прошли через неё
            for i in range(len(neighbours)):
                new_cost = costs[node] + self.__matrix[node][neighbours[i]]

                if new_cost < costs[neighbours[i]]:
                    costs[neighbours[i]] = new_cost
                    parents[neighbours[i]] = node

                    # отмечаем вершину и далее выбираем новую с минимальным расстоянием из не посещенных
            visited.append(node)
            node = self.__search_min_node(visited, costs)

        if costs[self.__end_vertex] == 1000000:
            return -1, -1

        # получаем путь от begin_vertex до end_vertex
        route = self.__get_route(parents)

        return costs[self.__end_vertex], route

    # получение соседей с минимальным расстоянием из не посещенных
    def __search_min_node(self, visited, costs):
        min_cost = 1000000
        node = 0
        for i in range(self.__matrix_len):
            if i not in visited and costs[i] < min_cost:
                min_cost = costs[i]
                node = i

        return node

    # получение пути между начальной и конечной вершинами
    def __get_route(self, parents):
        route = []
        vertex = self.__end_vertex

        # идем по родителям от конечной вершины
        while vertex != self.__begin_vertex:
            route.append([parents[vertex], vertex, self.__graph.weight(parents[vertex], vertex)])
            vertex = parents[vertex]

        # реверсируем массив, тк родителей писали в обратном порядке
        route.reverse()

        return route
