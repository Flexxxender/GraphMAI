class BridgesAndCutVertices:
    _cut_vertcies = []
    _bridges = []

    # инициализируем граф, ассоциативную матрицу и tin tup, времена входа для алгоритма поиска
    def __init__(self, graph):
        self._graph = graph
        self._associated_matrix = self._graph.associated_matrix()
        self._tin = [0] * len(self._associated_matrix)
        self._tup = [0] * len(self._associated_matrix)

        self.__find_bridges_and_cut_vertices()

    # получаем мосты
    @property
    def bridges(self):
        return self._bridges

    # получаем точки сочленения (шарниры)
    @property
    def cut_vertices(self):
        return sorted(self._cut_vertcies)

    # нахождение мостов и шарниров в графе
    def __find_bridges_and_cut_vertices(self):
        marked = []
        vertices = [i for i in range(len(self._associated_matrix))]

        # пока не все вершины обработаны - вызываем DFS и убираем вершины, входящие в дерево обхода DFS
        while len(vertices):
            one_component = self.__bridges_and_cut_vertices_DFS(vertices[0], self._bridges, self._cut_vertcies, marked)

            for vertice in one_component:
                if vertice in vertices:
                    vertices.remove(vertice)

    # DFS для нахождения мостов и шарниров в графе
    def __bridges_and_cut_vertices_DFS(self, v, bridges, cut_vertices, marked, p=-1):
        marked.append(v)
        component = [v]

        # при входе в новую вершину tin = tup и берем tin предыдущей + 1
        self._tup[v] = self._tin[v] = (1 if p == -1 else self._tin[p] + 1)
        children = 0

        for u in self._graph.adjacency_list(self._associated_matrix, v):
            if u == p:  # (v, u) ведет в предка - не интересует
                continue

            if u in marked:  # нашли обратное ребро (v, u)
                self._tup[v] = min(self._tup[v], self._tin[u])

            else:  # нашли прямое ребро (v, u)
                component.extend(self.__bridges_and_cut_vertices_DFS(u, bridges, cut_vertices, marked, v))
                self._tup[v] = min(self._tup[v], self._tup[u])
                children += 1

                # условие для моста
                if self._tin[v] < self._tup[u]:
                    bridges.append([v + 1, u + 1])

                # условие для шарнира
                if self._tin[v] <= self._tup[u] and p != -1 and v + 1 not in cut_vertices:
                    cut_vertices.append(v + 1)

        # условие для шарнира в начальной вершине DFS
        if p == -1 and children > 1:
            cut_vertices.append(v + 1)

        return component
