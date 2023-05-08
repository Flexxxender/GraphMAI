class AlgBoruvka:
    def __init__(self, graph):
        self.__graph = graph
        self.__matrix = graph.associated_matrix()
        self.__matrix_len = len(self.__matrix)

    # нахождение минимального остовного дерева
    def spanning_tree(self):
        tree = []
        edges = self.__graph.list_of_edges()
        parents, size = self.__init_DSU() # инициализация DSU
        
        # количество компонент связности, изначально каждая вершина это отдельная компонента
        components = self.__matrix_len
        
        # индекс минимального ребра из каждой компоненты связности
        min_edge = [-1 for i in range(self.__matrix_len)]

        # пока не останется одна компонента связности
        while components != 1:
            # изнаально минимальное ребро для каждой компоненты равно -1
            for i in range(self.__matrix_len):
                min_edge[i] = -1

            # перебираем все ребра 
            for edge in edges:
                # если ребро соединяет одинаковые компоненты связности - пропускаем
                if self.__root(edge[0], parents) == self.__root(edge[1], parents):
                    continue

                # находим лидера вершины v из ребра (v, u) и если минимальное ребро не найдено 
                # или вес просматриваемого ребра меньше веса минимального ребра - 
                # запоминаем индекс минимального ребра для leader_v вершины
                leader_v = self.__root(edge[0], parents)
                if min_edge[leader_v] == -1 or edge[2] < min_edge[leader_v][2]:
                    min_edge[leader_v] = edge
                
                # аналогично для лидера вершины u из ребра (v, u)
                leader_u = self.__root(edge[1], parents)
                if min_edge[leader_u] == -1 or edge[2] < min_edge[leader_u][2]:
                    min_edge[leader_u] = edge

            # если минимальное ребро найдено - объединяем компоненты, добавляем ребро в дерево
            # а также количество компонент связности уменьшаем на единицу
            for i in range(self.__matrix_len):
                if min_edge[i] != -1 and self.__union(min_edge[i][0], min_edge[i][1], parents, size):
                    tree.append([min_edge[i][0] + 1, min_edge[i][1] + 1, min_edge[i][2]])
                    components -= 1

        # подсчет веса полученного дерева
        tree_weight = sum((tree[i][2] for i in range(len(tree))))

        return tree, tree_weight

    # DSU аналогичное алгоритму Краскала с эвристиками сжатия путей и весов деревьев
    def __init_DSU(self):
        p = [i for i in range(self.__matrix_len)]
        s = [1] * self.__matrix_len
        return p, s

    def __root(self, vertice, parent):
        if parent[vertice] != vertice:
            parent[vertice] = self.__root(parent[vertice], parent)
        return parent[vertice]

    def __union(self, aa, bb, parent, size):
        a = self.__root(aa, parent)
        b = self.__root(bb, parent)
        if a == b:
            return False
        elif size[a] > size[b]:
            parent[b] = a
            size[a] += size[b]
        else:
            parent[a] = b
            size[b] += size[a]
        return True
