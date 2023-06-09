class Cell:
    parent = None  # родитель вершины
    full_distance = 0  # полное расстояние для вершины
    distance_from_start = 0  # расстояние до старта для вершины

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
