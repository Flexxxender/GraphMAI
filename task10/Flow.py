import copy


class FindMaxFlow:
    def __init__(self, graph):
        self._graph = graph
        self._matrix = graph.adjacency_matrix()
        self._matrix_len = len(self._matrix)
        self._source = self.__find_source()
        self._sink = self.__find_sink()
        self.flow_matrix, self.max_flow = self.edmonds_karp()

    # геттер для источника
    @property
    def source(self):
        return self._source

    # геттер для стока
    @property
    def sink(self):
        return self._sink

    # алгоритм Эдмондса-Карпа
    def edmonds_karp(self):
        if self._sink == -1 or self._source == -1:
            return -1, -1

        result = copy.deepcopy(self._matrix)
        ost = copy.deepcopy(self._matrix)

        while True:
            # пока путь от истока до стока существует
            way = self.__BFS(ost)
            if way == -1:
                break
            # получаем пропускную способность дуги
            way.sort(key=lambda edge: edge[2])
            min_edge = way[0][2]
            # обновляем матрицу пропускных способностей
            for edge in way:
                ost[edge[0]][edge[1]] -= min_edge
                ost[edge[1]][edge[0]] += min_edge

        # результирующую матрицу получаем как разность изначальной матрицы и остаточных пропускных способностей
        # в изначальной матрице записаны пропускные способности ребер, а в ost - остаточные пропускные способности
        for i in range(self._matrix_len):
            for j in range(self._matrix_len):
                if self._graph.is_edge(result, i, j):
                    result[i][j] -= ost[i][j]

        # значение максимального потока это входной поток на сток
        max_flow = 0
        for i in range(self._matrix_len):
            if self._graph.is_edge(result, i, self._sink):
                max_flow += result[i][self._sink]

        return result, max_flow

    # BFS для нахождения дополняющей цепи
    def __BFS(self, matrix):
        queue = [self._source]  # очередь, в которой изначально только источник
        is_sink = False  # флаг остановки, если дошли до стока

        visited = [False] * self._matrix_len  # массив посещенных вершин
        visited[self._source] = True

        parents = [-1] * self._matrix_len  # массив родителей для каждой вершины
        parents[self._source] = self._source

        while len(queue):
            # берем вершину из очереди и смотрим ее соседей
            current_vertex = queue.pop(0)
            neighbours = self._graph.adjacency_list(matrix, current_vertex)

            for neighbour in neighbours:
                # если сосед еще не посещен и еще можно пропустить поток
                if matrix[current_vertex][neighbour] != 0 and not visited[neighbour]:
                    # помечаем соседа, его родителем будет текущая вершина, а самого соседа заносим в конец очереди
                    visited[neighbour] = True
                    parents[neighbour] = current_vertex
                    queue.append(neighbour)
                    # если сосед является стоком - выходим, цепь найдена
                    if neighbour == self._sink:
                        is_sink = True
                        break
            if is_sink:
                break

        # критерий остановки - если все еще не дошли до стока
        if not is_sink:
            return -1

        # возвращаем дополняющую цепь
        return self.__get_route_for_BFS(parents, matrix)

    # получение дополнящей цепи минимального количества ребер
    def __get_route_for_BFS(self, parents, matrix):
        route = []
        vertex = self._sink
        # идем по родителям от стока, пока не дойдем до источника
        while vertex != self._source:
            route.append([parents[vertex], vertex, matrix[parents[vertex]][vertex]])
            vertex = parents[vertex]

        # реверсируем массив, тк родителей писали в обратном порядке
        route.reverse()

        return route

    # нахождение источника в сети (вершина, в которую ничего не входит)
    def __find_source(self):
        for i in range(self._matrix_len):
            is_source = True
            for j in range(self._matrix_len):
                if self._graph.is_edge(self._matrix, j, i):
                    is_source = False
                    continue
            if is_source:
                return i
        return -1

    # нахождение стока в сети (вершина, из которой ничего не выходит)
    def __find_sink(self):
        for i in range(self._matrix_len):
            is_sink = True
            for j in range(self._matrix_len):
                if self._graph.is_edge(self._matrix, i, j):
                    is_sink = False
                    continue
            if is_sink:
                return i
        return -1
