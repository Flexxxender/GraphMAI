from task0 import GraphModule as GraphModule


# модифицированный класс графа, расширяющий функционал обычного
class ModifiedGraph(GraphModule.Graph):
    def __init__(self, matrix):
        super().__init__(matrix)

    # добавить вершину в конец, соединив ее со всеми остальными нулевыми ребрами
    def add_vertex(self):
        for i in range(self._matrix_len):
            self._matrix[i].append(1000000)
        self._matrix.append([0] * (self._matrix_len + 1))
        self._matrix_len += 1
        return self._matrix

    # удалить указанную вершину
    def del_vertex(self, vertex):
        for i in range(self._matrix_len):
            self._matrix[i].pop(vertex)
        self._matrix.pop(vertex)
        self._matrix_len -= 1
        return self._matrix
    
    # является ли граф двудольным
    def is_bipartite(self):
        # изначально окрашена только стартовая вершина в первый цвет
        colors = [0] * self._matrix_len
        colors[0] = 1
        marked = []
        return self.__coloring_DFS(0, marked, colors)

    # DFS для окрашивания
    def __coloring_DFS(self, vertex, marked, colors):
        # маркируем вершину и смотрим ее цвет
        marked.append(vertex)
        current_color = colors[vertex]
        oposite_color = -1 if current_color == 1 else 1
        for neighbour in self.adjacency_list(self._matrix, vertex):
            if neighbour not in marked:
                # если сосед не окрашен - окрашиваем в противоположный
                if colors[neighbour] == 0:
                    colors[neighbour] = oposite_color
                # если сосед и так окрашен в противоположный - все хорошо    
                elif colors[neighbour] == oposite_color:
                    pass
                # иначе граф не может быть двудольным
                else:
                    return -1
                self.__coloring_DFS(neighbour, marked, colors)
        return colors