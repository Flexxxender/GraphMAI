from task10.Flow import FindMaxFlow

class Matching:
    def __init__(self, modified_graph):
        self._colors = modified_graph.is_bipartite()
        self._graph = modified_graph

    def __add_sink_and_source(self):
        self._colors.extend([0,0])
        # добавили сток
        for i in range(self._graph._matrix_len):
            # в него входят только вершины из одной доли и ничего не выходит
            if self._colors[i] == 1:
                self._graph._matrix[i].append(1)
            else:
                self._graph._matrix[i].append(1000000)
        self._graph._matrix.append([1000000] * (self._graph._matrix_len + 1))
        self._graph._matrix_len += 1

        # добавили источник
        for i in range(self._graph._matrix_len):
            # в него ничего не входит
            self._graph._matrix[i].append(1000000)
        self._graph._matrix.append([1000000] * (self._graph._matrix_len + 1))
        self._graph._matrix_len += 1

        for i in range(self._graph._matrix_len):
            # если вершина из другой доли - в нее входит ребро из источника
            if self._colors[i] == -1:
                self._graph._matrix[self._graph._matrix_len - 1][i] = 1

    # сделать граф ориентрованным
    def __make_directed_graph(self):
        for i in range(self._graph._matrix_len):
            for j in range(self._graph._matrix_len):
                # если есть ребро из первой половины во вторую - убираем обратное
                if self._graph._matrix[i][j] != 1000000 and self._colors[i] == -1 and self._colors[j] == 1:
                    self._graph._matrix[j][i] = 1000000


    def find_max_matching(self):
        # если граф не двудольный, то выходим
        if self._colors == -1:
            return -1
        
        # добавили сток и источник и сделали граф правильно ориентированным
        self.__add_sink_and_source()
        self.__make_directed_graph()

        # запускаем алгоритм Эдмондса-Карпа и находим максимальный поток в графе
        new_graph = FindMaxFlow(self._graph)
        result, useless = new_graph._edmonds_karp()

        # возвращаем матрицу графа к исходному состоянию
        self.delete_last_vertex(self._graph._matrix)
        self.delete_last_vertex(self._graph._matrix)
        self._graph._matrix_len -= 2

        # убираем источник и сток из результирующей матрицы
        self.delete_last_vertex(result)
        self.delete_last_vertex(result)

        return result
    
    @staticmethod
    def delete_last_vertex(array):
        for i in range (len(array)):
            array[i].pop(len(array) - 1)
        array.pop(len(array) -1)
