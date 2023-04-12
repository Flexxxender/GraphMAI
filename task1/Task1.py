import copy


class GraphFeatures:

    # конструктор, в котором инициализируются матрица смежности и матрица достижимости графа
    # а также их длины, является ли граф связным и ориентированным
    def __init__(self, graph):
        self.__distance_matrix = self.__floyd_warshall(graph.adjacency_matrix())
        self.__adjacency_matrix = graph.adjacency_matrix()
        
        self.__dist_matrix_len = len(self.__distance_matrix)
        self.__adj_matrix_len = len(self.__adjacency_matrix)

        self.is_connected = self.__is_connected()
        self.is_directed = graph.is_directed()

    # алгоритм Флойда-Уоршелла
    def __floyd_warshall(self, matrix):
        matrix_len = len(matrix)
        for k in range(matrix_len):
            for i in range(matrix_len):
                for j in range(matrix_len):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]) if i != j else 0
        return matrix

    # возвращает true, если граф сильносвязный, иначе false
    def __is_connected(self):
        # тк матрица сильной связности равна произведению матрицы достижимости
        # на транспонированную матрицу достижимости, смотрим, что (i,j) и (j,i) != 10000000
        for i in range(self.__dist_matrix_len):
            for j in range(i, self.__dist_matrix_len):
                if not (self.__distance_matrix[i][j] != 1000000 and self.__distance_matrix[j][i] != 1000000):
                    return False
        return True

    # возвращает матрицу достижимости (копию, чтобы избежать изменений матрицы в классе)
    def distance_matrix(self):
        return copy.deepcopy(self.__distance_matrix)

    def eccentricity(self):
        if not self.is_connected:
            return -1

        eccentricity = []
        maxim = 0
        
        # ищем максимальные расстояния из вершин, то есть эксцентриситет каждой
        for rows in self.__distance_matrix:
            maxim = max(rows)
            eccentricity.append(maxim)
            
        return eccentricity

    # нахождение радиуса в графе
    def radius(self):
        if not self.is_connected:
            return -1
        
        return min(self.eccentricity())

    # нахождение диаметра в графе
    def diameter(self):
        if not self.is_connected:
            return -1
        
        return max(self.eccentricity())

    # нахождение центральных вершин в графе (вершин с эксцентриситетом равным радиусу графа)
    def central_vertices(self):
        if not self.is_connected:
            return -1
        
        graph_eccentricity = self.eccentricity()
        radius = self.radius()
        vertices = []

        # если эксцентриситет какой-либо из вершин совпал с радиусом графа - добавляем
        for index, vert_eccentricity in enumerate(graph_eccentricity):
            if vert_eccentricity == radius:
                vertices.append(index + 1)
        return vertices

    # нахождение периферийных вершин (вершин с эксцентриситетом равным диаметру графа)
    def peripheral_vertices(self):
        if not self.is_connected:
            return -1
        
        graph_eccentricity = self.eccentricity()
        diameter = self.diameter()
        vertices = []
        
        # если эксцентриситет какой-либо из вершин совпал с диаметром графа - добавляем
        for index, vert_eccentricity in enumerate(graph_eccentricity):
            if vert_eccentricity == diameter:
                vertices.append(index + 1)
        return vertices

    # возвращает вектор степеней вершин в графе
    def vector_degrees(self):
        # значит требуются просто степени вершин
        if not self.is_directed: 
            vector = []
            # идем по каждой строчке и считаем существующие ребра
            for rows in self.__adjacency_matrix:
                vector.append(sum([1 for j in rows if j != 1000000]))
            return vector
        
        # иначе мы имеемм дело с орграфом, то есть требуется посчитать
        # степени захода и исхода для каждой из вершин
        vector_plus = [0 for i in range(self.__adj_matrix_len)]
        vector_minus = [0 for i in range(self.__adj_matrix_len)]

        for i in range(self.__adj_matrix_len):
            for j in range(self.__adj_matrix_len):
                # если ребро (i, j) - оно исходит из вершины i
                if (self.__adjacency_matrix[i][j] != 1000000):
                    vector_minus[i] += 1
                # если ребро (j, i) - оно заходит в вершину i
                if (self.__adjacency_matrix[j][i] != 1000000):
                    vector_plus[i] += 1

        return vector_plus, vector_minus
