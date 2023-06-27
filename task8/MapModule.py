from task8.CellModule import Cell


class Map:
    def __init__(self, matrix):
        self._matrix = matrix
        self.matrix_len = len(self._matrix)

    # получить соседей вершины
    def neighbours(self, cell: Cell) -> [Cell]:
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # можем двигаться вверх влево вправо вниз
        neighbours = []

        for step in steps:
            # считаем и проверяем координаты гипотетического соседа на корректность,
            # чтобы не взять несуществующую клетку как соседа
            neighbour_cords = [cell.x + step[0], cell.y + step[1]]
            if neighbour_cords[0] < 0 or neighbour_cords[1] < 0:
                continue
            if neighbour_cords[0] >= len(self._matrix) or neighbour_cords[1] >= len(self._matrix):
                continue
            neighbours.append(Cell(neighbour_cords[0], neighbour_cords[1]))

        return neighbours

    # подсчет расстояния между клетками
    def distance(self, u: Cell, v: Cell):
        return abs(u.x - v.x) + abs(u.y - v.y) + abs(self.height(u.x, u.y) - self.height(v.x, v.y))

    # индексатор (почти)
    def height(self, x, y):
        return self._matrix[x][y]
