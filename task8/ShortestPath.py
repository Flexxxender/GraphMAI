import math

from task8.Cell import Cell
from task8.Map import Map


class ShortestPath:

    def __init__(self, map: Map):
        self.__map = map

    def a_star(self, begin_cell: Cell, end_cell: Cell, h):
        open_cells = [begin_cell]  # доступные клетки
        closed_cells = []  # обработанные клетки
        current_cell = begin_cell
        current_cell.parent = current_cell
        current_cell.distance_from_start = 0
        current_cell.full_distance = 0

        # пока текущая вершина не равна конечной
        while current_cell != end_cell:
            # нахождение следующей вершины с минимальным расстоянием из доступных
            current_cell = self.__find_min_cell(open_cells)
            # убираем вершину из доступных и кладем в обработанные
            open_cells.remove(current_cell)
            closed_cells.append(current_cell)

            # получаем соседей и проходимся по ним
            neighbours = self.__map.neighbours(current_cell)
            for neighbour in neighbours:
                # если сосед уже обработан - пропускаем
                if self.__in_array(neighbour, closed_cells) != Cell(-1, -1):
                    continue

                new_cell = self.__in_array(neighbour, open_cells)
                # если сосед в доступных клетках
                if new_cell != Cell(-1, -1):
                    # пересчитываем расстояние до старта у соседа
                    new_start_distance = current_cell.distance_from_start + \
                                         self.__map.distance(current_cell, new_cell)
                    # если расстояние стало меньше - переписываем родителя, расстояние и полное расстояние
                    if new_start_distance < new_cell.distance_from_start:
                        new_cell.parent = current_cell
                        new_cell.distance_from_start = new_start_distance
                        new_cell.full_distance = new_cell.distance_from_start + h(new_cell, end_cell)
                # если пришли в соседа впервые
                else:
                    # записываем родителя, расстояние до старта и полное расстояние и добавляем в доступные клетки
                    neighbour.parent = current_cell
                    neighbour.distance_from_start = current_cell.distance_from_start + \
                                                    self.__map.distance(neighbour, current_cell)
                    neighbour.full_distance = neighbour.distance_from_start + h(neighbour, end_cell)
                    open_cells.append(neighbour)

        # получение пути, длины пути, а также процент просмотренных алгоритмом клеток от общего их числа
        path = self.__get_path(begin_cell, current_cell)
        length_path = current_cell.distance_from_start
        percent = len(closed_cells) / math.pow(self.__map.matrix_len, 2) * 100

        return path, percent, length_path

    # есть ли элемент в массиве
    @staticmethod
    def __in_array(u: Cell, array: [Cell]):
        for cell in array:
            if u == cell:
                return cell
        return Cell(-1, -1)

    # найти следующую клетку с минимальным полным расстоянием
    @staticmethod
    def __find_min_cell(open_cells: [Cell]):
        minimum = 1000000000
        min_i = -1
        for index, cell in enumerate(open_cells):
            if cell.full_distance < minimum:
                minimum = cell.full_distance
                min_i = index
        return open_cells[min_i]

    # восстановление маршрута
    @staticmethod
    def __get_path(begin_cell: Cell, end_cell: Cell):
        path = [end_cell]
        cell = end_cell
        # идем с последней клетки и по родителям - затем реверсируем массив
        while cell != begin_cell:
            cell = cell.parent
            path.append(cell)
        path.reverse()
        return path
