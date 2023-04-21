from abc import ABC


class GraphConnectivity(ABC):
    def __init__(self, graph):
        self._adjacency_matrix = graph.adjacency_matrix()
        self.__adj_matrix_len = len(self._adjacency_matrix)

    def BFS(self, vertex, matrix):
        queue = [vertex]
        marked_vertices = [vertex]

        while len(queue):
            current_vertex = queue.pop(0)
            neighbours = self.adjacency_list(matrix, current_vertex)
            for neighbour in neighbours:
                if neighbour not in marked_vertices:
                    queue.append(neighbour)
                    marked_vertices.append(neighbour)

        marked_vertices.sort()
        return marked_vertices

    def is_connected(self, matrix):
        if len(self.BFS(0, matrix)) != self.__adj_matrix_len:
            return False
        return True

    def count_connected_components(self, matrix):
        vertices = [int(i) for i in range(len(matrix))]
        counter = 0
        components = []

        for current_vertex in vertices:
            component = self.BFS(current_vertex, matrix)

            for vertex in component:
                vertices.pop(vertices.index(vertex))

            counter += 1
            components.append(component)

        return counter, components

    def DFS(self, vertex, counter, counters, matrix):
        vertices = [vertex]
        stack = [vertex]

        while len(stack):
            current_vertex = stack.pop()

            counter[0] += 1
            counters[current_vertex] = counter[0]

            unmarked_neighbours = []
            neighbours = self.adjacency_list(matrix, current_vertex)
            for vertex in neighbours:
                if counters[vertex] == 0:
                    unmarked_neighbours.append(vertex)

            for vertex in unmarked_neighbours:
                stack.append(current_vertex)
                stack.append(vertex)
                vertices.append(vertex)
                break

        return vertices

    @staticmethod
    def adjacency_list(matrix, vert):
        vertices = []
        for i in range(len(matrix)):
            if matrix[vert][i] != 1000000 and vert != i:
                vertices.append(i)
        return vertices
