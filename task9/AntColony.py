import math
import random


class AntColony:
    alpha = 2  # показатель важности феромонного следа
    beta = 5  # показатель важности близости вершин
    p = 0.4  # коэффициент рассеяния феромона
    count_iter = 500  # количество итераций

    def __init__(self, graph):
        self._graph = graph
        self._matrix = self._graph.adjacency_matrix()
        self.pheromones = [[1 if i != j else 0 for i in range(len(self._matrix))] for j in range(len(self._matrix))]
        self.q = sum(self._matrix[0][i] for i in range(len(self._matrix))) # пропорционально длине пути

    def ant_colony(self, begin_vertex):
        res = []
        n = self.count_iter
        count_vertex = len(self._matrix)

        for n in range(n, 0, -1):
            pathes = []
            # садим муравья на каждый город
            for i in range(len(self._matrix)):
                visited = [False] * len(self._matrix)
                visited[i] = True
                path = self.Path()
                count_cities = count_vertex - 1
                current = i

                # пока муравей не побывал во всех городах
                while count_cities != 0:
                    # получаем непосещенных соседей
                    neighbours = self._graph.adjacency_list(self._matrix, current)
                    for neighbour in neighbours:
                        if visited[neighbour]:
                            neighbours.remove(neighbour)

                    denominator = sum(self.desire(current, n) for n in neighbours)
                    # находим вероятности перехода в соседние города
                    probabilities = [self.desire(current, n)/denominator for n in neighbours]
                    for j in range(1, len(probabilities)):
                        probabilities[j] += probabilities[j - 1]

                    # получаем следующий город, в который пойдет муравей, добавляем его в посещенные
                    # а также заполняем маршрут ребром, которое только что прошел муравей
                    next = self.random(probabilities, neighbours)
                    visited[next] = True
                    count_cities -= 1
                    path.list_of_edges.append([current, next, self._matrix[current][next]])
                    path.length += self._matrix[current][next]

                    # меняем следующую вершину
                    current = next

                pathes.append(path)

            # испаряем феромон
            for i in range(len(self.pheromones)):
                for j in range(len(self.pheromones)):
                    self.pheromones[i][j] = self.pheromones[i][j] * (1-self.p)

            # обновляем феромоны
            for path in pathes:
                for edge in path.list_of_edges:
                    self.pheromones[edge[0]][edge[1]] = self.pheromones[edge[0]][edge[1]] \
                                                        + self.q / path.length
                    self.pheromones[edge[1]][edge[0]] = self.pheromones[edge[0]][edge[1]]

        # формируем лучший путь
        current = begin_vertex
        visited = [False] * len(self._matrix)
        visited[current] = True
        k = 1
        while  k != len(self._matrix):
            max_i = -1
            max = -1000000
            # идем от начальной вершины по максимальному феромонному следу
            for i in range(len(self._matrix)):
                if self.pheromones[current][i] > max and not visited[i]:
                    max = self.pheromones[current][i]
                    max_i = i

            visited[max_i] = True
            k += 1
            next = max_i
            res.append([current, next, self._matrix[current][next]])
            current = next

        res.append([next, begin_vertex, self._matrix[next][begin_vertex]])
        return res

    # желание муравья пойти из i-ого города в j-ый
    def desire(self, i, j):
        return math.pow(self.pheromones[i][j], self.alpha) / math.pow(self._matrix[i][j], self.beta)

    # вероятность того, что муравей пойдет в j-ый город
    def probability(self, i, j, neighbours):
        return self.desire(i, j) / sum(self.desire(i, n) for n in neighbours)

    # рандомное число, отвечающее за город, в который пойдет муравей
    @staticmethod
    def random(p, neighbours):
        rand = random.random()
        i = 0
        res = neighbours[i]
        while rand > p[i]:
            i += 1
            res = neighbours[i]
        return res

    class Path:
        def __init__(self):
            self.length = 0
            self.list_of_edges = []