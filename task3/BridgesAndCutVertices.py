class BridgesAndCutVertices:
    cut_vertcies = []
    bridges = []

    def __init__(self, graph):
        self.__graph = graph
        self.__associated_matrix = self.__graph.associated_matrix()
        self.tin = [0] * len(self.__associated_matrix)
        self.tup = [0] * len(self.__associated_matrix)

        self.__find_bridges_and_cut_vertices()

    # получаем мосты
    def get_bridges(self):
        return self.bridges

    # получаем точки сочленения (шарниры)
    def get_cut_vertices(self):
        return self.cut_vertcies

    # нахождение мостов и шарниров в графе
    def __find_bridges_and_cut_vertices(self):
        marked = []
        vertices = [i for i in range(len(self.__associated_matrix))]

        # пока не все вершины обработаны - вызываем DFS и убираем вершины, входящие в дерево обхода DFS
        while len(vertices):
            one_component = self.__bridges_and_cut_vertices_DFS(vertices[0], self.bridges, self.cut_vertcies, marked)

            for vertice in one_component:
                if vertice in vertices:
                    vertices.remove(vertice)

    def __bridges_and_cut_vertices_DFS(self, v, bridges, cut_vertices, marked, p=-1):
        marked.append(v)
        component = [v]

        # при входе в новую вершину tin = tup и берем tin предыдущей + 1
        self.tup[v] = self.tin[v] = (1 if p == -1 else self.tin[p] + 1)
        children = 0

        for u in self.__graph.adjacency_list(self.__associated_matrix, v):
            if u == p:  # (v, u) ведет в предка - не интересует
                continue

            if u in marked:  # нашли обратное ребро (v, u)
                self.tup[v] = min(self.tup[v], self.tin[u])

            else:  # нашли прямое ребро (v, u)
                component.extend(self.__bridges_and_cut_vertices_DFS(u, bridges, cut_vertices, marked, v))
                self.tup[v] = min(self.tup[v], self.tup[u])
                children += 1

                # условие для моста
                if self.tin[v] < self.tup[u]:
                    bridges.append([v + 1, u + 1])

                # условие для шарнира
                if self.tin[v] <= self.tup[u] and p != -1 and v not in cut_vertices:
                    cut_vertices.append(v + 1)

        # условие для шарнира в начальной вершине DFS
        if p == -1 and children > 1:
            cut_vertices.append(v)

        return component
