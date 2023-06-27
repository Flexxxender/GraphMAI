import math
from task0 import Strategy, OutputModule, ParserModule
from task8 import CellModule, MapModule, ShortestPath

if __name__ == '__main__':
    # словарь эвристик для а-стара
    heuristics = [lambda u, v: abs(u.x - v.x) + abs(u.y - v.y),  # манхэттеновская
                  lambda u, v: max(abs(u.x - v.x), abs(u.y - v.y)),  # чебышева
                  lambda u, v: math.sqrt(pow((u.x - v.x), 2) + pow((u.y - v.y), 2)),  # евклидова
                  lambda u, v: 0]  # без эвристики (классический алгоритм Дейкстры)
    # название всех эвристик
    heuristics_name = ["Manhattan distance", "Chebyshev distance", "Euclidean distance", "Without heuristic"]

    output = OutputModule.Output()
    parser = ParserModule.Parser(8)
    args = parser.args
    output.check_file_needed(args.o)

    try:
        map = MapModule.Map(Strategy.a_star_matrix_strategy(args.m))  # создаем карту
        shortest_path = ShortestPath.ShortestPath(map)  # запускаем алгоритм а-стар
        n = [int(args.n[0]), int(args.n[1])]  # координаты первой вершины
        d = [int(args.d[0]), int(args.d[1])]  # координаты второй вершины
        count_heuristics = 0  # счетчик текущей эвристики, чтобы выводить ее название

        for h in heuristics:
            # вывод длины пути, самого пути и отношения просмотренных клеток к их общему числу для каждой эвристики
            path, percent, path_len = shortest_path.a_star(CellModule.Cell(n[0], n[1]), CellModule.Cell(d[0], d[1]), h)

            output.write(heuristics_name[count_heuristics])
            output.write(f"{path_len} - length of path between {n[0], n[1]} and {d[0], d[1]} points.")
            output.write("Path:")

            count_heuristics += 1
            for cell in path:
                output.write(f"{cell.x, cell.y} ", end='')

            output.write()
            output.write(f"percent viewing algorithmic cells of their total number: {percent}", end='\n\n')
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
