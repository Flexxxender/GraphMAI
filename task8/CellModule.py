class Cell:
    parent = None  # родитель вершины
    full_distance = 0  # полное расстояние для вершины
    distance_from_start = 0  # расстояние до старта для вершины

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # переопределяем оператор сравнения двух клеток (берутся их координаты)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
