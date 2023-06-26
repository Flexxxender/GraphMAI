from task6 import BellmanFord, Dijkstra


class AlgJohnson:
    # принимается на вход модифицированный класс графа, где добавляются методы
    # добавления и удаления вершины в графе
    def __init__(self, modified_graph):
        self._graph = modified_graph
        self.distances, self.negative_edge = self.__johnson()

    # алгортим Джонсона
    def __johnson(self):
        # добавляется новая вершина q и ребра нулевого веса от этой вершины ко всем остальным
        self._graph.add_vertex()

        # используется алгоритм Беллмана-Форда для расчета растояний от q до всех остальных вершин
        h = BellmanFord.AlgBellmanFord(self._graph).distances(len(self._graph._matrix) - 1)

        # вершина удаляется, далее работа будет с изначальным графом и его матрицей смежности
        self._graph.del_vertex(len(self._graph._matrix) - 1)

        # если Б.Ф. нашел цикл отрицательного веса, то работа алгоритма завершается
        if h == -10:
            return -10, True

        # флаг для проверки на отрицательное ребро
        negative_edge = False
        for dist in h:
            if dist < 0:
                negative_edge = True

        # делаем копию матрицы, чтобы затем после пересчитываний весов все вернуть как было
        matrix_copy = self._graph.adjacency_matrix()

        # пересчитываются веса ребер
        for i in range(len(self._graph._matrix)):
            for j in range(len(self._graph._matrix)):
                self._graph._matrix[i][j] = self._graph._matrix[i][j] + h[i] - h[j] \
                    if self._graph.is_edge(self._graph._matrix, i, j) else 1000000

        # из каждой вершины запускаем алгоритм Дейкстры
        d = [0] * len(self._graph._matrix)
        for i in range(len(self._graph._matrix)):
            d[i] = Dijkstra.AlgDijkstra(self._graph).distances(i)

        # для найденных расстояний вычисляем исходное значение
        for i in range(len(self._graph._matrix)):
            for j in range(len(self._graph._matrix)):
                d[i][j] = d[i][j] + h[j] - h[i] if d[i][j] != 1000000 else 1000000

        # возвращаем матрицу в исходное состояние
        self._graph._matrix = matrix_copy

        return d, negative_edge
