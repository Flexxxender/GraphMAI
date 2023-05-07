class AlgPrima:
    def __init__(self, graph):
        self.__graph = graph
        self.__matrix = graph.associated_matrix()
        self.__matrix_len = len(self.__matrix)

    # нахождение минимального остовного дерева
    def spanning_tree(self):
        tree = []
        edges = self.__graph.list_of_edges()
        edges.sort(key=lambda edge: edge[2]) # нашли и отортировали все ребра графа по весу
        vertices = [0] * self.__matrix_len # массив посещенных вершин, изначально ни одну мы не посетили
        vertices[0] = 1 # посетили первую, с которой все начнем
        edge_adj = [] # смежное ребро, которое будем каждый раз добавлять

        # пока все вершины не посещены или все ребра не обработаны
        while min(vertices) != 1 and len(edges):
            # идем по ребрам и находим первое ребро, инцидентное любой из посещенных вершин
            # оно будет обладать минимально возможным весом, ибо ребра отсортированы
            for i in range(len(edges)):
                if (vertices[edges[i][0]] + vertices[edges[i][1]]) % 2:
                    edge_adj = edges[i]
                    break

            # добавляем ребро в дерево, его само удаляем из всех ребер, а также
            # отмечаем инцидентные ребру вершины как посещенные
            tree.append([edge_adj[0] + 1, edge_adj[1] + 1, edge_adj[2]])
            edges.remove(edge_adj)
            vertices[edge_adj[1]] = vertices[edge_adj[0]] = 1

        # подсчет веса полученного дерева
        tree_weight = sum((tree[i][2] for i in range(len(tree))))
        
        return tree, tree_weight

