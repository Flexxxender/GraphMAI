class AlgKruskal:
    def __init__(self, graph):
        self.__graph = graph
        self.__matrix = graph.associated_matrix()
        self.__matrix_len = len(self.__matrix)


    '''----------------Реализация как из лекций, но по-дедовски------------------'''
    # def spanning_tree(self): # нахождение минимального остовного дерева
    #     tree = []
    #     # получили и отсортировали ребра графа по весу
    #     edges = self.__graph.list_of_edges()
    #     edges.sort(key=lambda edge: edge[2])
    #     # принадлежность вершин к компонентам связности
    #     vertices_belongs = [int(i) for i in range(self.__matrix_len)]
    
    #     # пока не просмотрели все ребра или все вершины не принадлежат одной компоненте
    #     while len(edges) and (min(vertices_belongs) != max(vertices_belongs)):
    #         # если вершины в разных компонентах связности - добавляем ребро в дерево
    #         # а также объединяем компоненты связности обычным способом
    #         if vertices_belongs[edges[0][0]] != vertices_belongs[edges[0][1]]:
    
    #             tree.append([edges[0][0] + 1, edges[0][1] + 1, edges[0][2]])
    
    #             for i in range(len(vertices_belongs)):
    #                 if vertices_belongs[i] == vertices_belongs[edges[0][0]] and i != edges[0][0]:
    #                     vertices_belongs[i] = vertices_belongs[edges[0][1]]
    #             vertices_belongs[edges[0][0]] = vertices_belongs[edges[0][1]]

    #         # удаляем обработанное ребро    
    #         edges.pop(0)
    
    #     # подсчет веса полученного дерева
    #     tree_weight = sum((tree[i][2] for i in range(len(tree))))
    
    #     return tree, tree_weight

    '''----Реализация через систему непересекающихся множеств - DSU (disjoint-set-union)---
       На последнем тесте графа на 2 тысячи вершин работает в среднем в 9-10 раз быстрее'''
    def spanning_tree(self): # нахождение минимального остовного дерева
        parents, size = self.__init_DSU() # инициализация DSU
        edges = self.__graph.list_of_edges()
        edges.sort(key=lambda edge: edge[2]) # нашли и отсортировали все ребра графа по весу
        tree = []

        # идем по всем ребрам и если находим ребро, у которого лидеры обеих вершин разные, 
        # то есть они принадлежат разным компонентам связности - добавляем его в дерево,
        # а компоненты связности объединяем
        for edge in edges:
            if self.__root(edge[0], parents) != self.__root(edge[1], parents):
                tree.append(edge)
                self.__union(edge[0], edge[1], parents, size)

        # подсчет веса полученного дерева
        tree_weight = sum((tree[i][2] for i in range(len(tree))))

        return tree, tree_weight

    # инициализация массивов родителей и весов деревьев
    def __init_DSU(self):
        p = [i for i in range(self.__matrix_len)] # родитель каждой вершины - она сама
        s = [1] * self.__matrix_len # вес каждого дерева единица
        return p, s

    # нахождение лидера вершины - принадлежность к компоненте связности
    def __root(self, vertice, parent):
        # если эта вершина не родитель самой себя - возвращаем ее родителя, 
        # который будет лидером этой компоненты связности
        if parent[vertice] != vertice:
            parent[vertice] = self.__root(parent[vertice], parent) # эвристика сжатия путей
        return parent[vertice]

    # объединение двух компонент связности
    def __union(self, aa, bb, parent, size):
        # находим лидеров двух компонент связности
        a = self.__root(aa, parent)
        b = self.__root(bb, parent)

        # весовая эвристика - всегда добавляем меньшее дерево к большему, 
        # чтобы не увеличивать асимптотику нахождения корня в дереве
        if size[a] > size[b]:
            parent[b] = a
            size[a] += size[b]
        else:
            parent[a] = b
            size[b] += size[a]