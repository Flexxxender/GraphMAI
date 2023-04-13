from abc import ABC


class GraphConnectivity(ABC):
    def __init__(self, graph):
        self._adjacency_matrix = graph.adjacency_matrix()
        self.__adj_matrix_len = len(self._adjacency_matrix)

    def BFS(self, vertex, matrix):
        queue = []
        marked_vertices = set()
        queue.append(vertex)
        marked_vertices.add(vertex)

        while len(queue):
            current_vertex = queue.pop(0)
            neighbours = self.adjacency_list(matrix, current_vertex)
            for neighbour in neighbours:
                if neighbour not in marked_vertices:
                    queue.append(neighbour)
                    marked_vertices.add(neighbour)

        return marked_vertices

    def is_connected(self, matrix):
        if len(self.BFS(0, matrix)) != self.__adj_matrix_len:
            return False
        return True

    def count_connected_components(self, matrix):
        vertices = set(int(i) for i in range(len(matrix)))
        counter = 0
        components = set()

        for vertex in vertices:
            component = self.BFS(vertex, matrix)
            vertices -= component
            counter += 1
            components.add(component)

        return counter, components

    def DFS(self, vertex, counter, counters, matrix):
        vertices = []
        stack = [vertex]

        while len(stack):
            current_vertex = stack.pop()

            if counters[current_vertex] == 0:
                vertices.append(current_vertex)
            counter += 1
            counters[current_vertex] = counter

            unmarked_neighbours = []
            neighbours = self.adjacency_list(matrix, current_vertex)
            for vertex in neighbours:
                if counters[vertex] == 0:
                    unmarked_neighbours.append(vertex)

            for vertex in unmarked_neighbours:
                stack.append(current_vertex)
                stack.append(vertex)
                break

        return vertices

    @staticmethod
    def adjacency_list(matrix, vert):
        vertices = []
        for i in range(len(matrix)):
            if matrix[vert][i] != 1000000 and vert != i:
                vertices.append(i)
        return vertices
