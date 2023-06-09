import argparse, math
from task0 import Strategy, Output
from task8 import Cell, Map, ShortestPath


# создание парсера, который будет считывать флаги исходного файла
# и также выходного, если потребуется
def create_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-m', default=False)
    argument_parser.add_argument('-o', default=False)

    argument_parser.add_argument('-n', nargs=2)
    argument_parser.add_argument('-d', nargs=2)

    return argument_parser


# проверка на нужду выходного файла
def check_file_needed(arg_o):
    if arg_o:
        # если файл нужен - меняем поток вывода из консоли на файл
        output.switch_to_file_output(arg_o)
        # очищаем файл путем открытия его для записи перед основной работой
        with open(arg_o, "w") as file:
            file.write("")


if __name__ == '__main__':
    heuristics = [lambda u, v: abs(u.x - v.x) + abs(u.y - v.y),
                  lambda u, v: max(abs(u.x - v.x), abs(u.y - v.y)),
                  lambda u, v: math.sqrt(pow((u.x - v.x), 2) + pow((u.y - v.y), 2)),
                  lambda u, v: 0]

    heuristics_name = ["Manhattan distance", "Chebyshev distance", "Euclidean distance", "Without heuristic"]

    output = Output.Output()  # создаем экземпляр класса Output из модуля Output
    parser = create_parser()  # создаем парсер
    args = parser.parse_args()  # получаем все флаги этого парсера
    check_file_needed(args.o)

    map = Map.Map(Strategy.a_star_matrix_strategy(args.m))
    shortest_path = ShortestPath.ShortestPath(map)
    n = [int(args.n[0]), int(args.n[1])]
    d = [int(args.d[0]), int(args.d[1])]
    count_heuristics = 0

    for h in heuristics:
        path, percent, path_length = shortest_path.a_star(Cell.Cell(n[0], n[1]), Cell.Cell(d[0], d[1]), h)
        output.write(heuristics_name[count_heuristics])
        output.write(f"{path_length} - length of path between {n[0], n[1]} and {d[0], d[1]} points.")
        output.write("Path:")
        count_heuristics += 1
        for cell in path:
            output.write(f"{cell.x, cell.y} ", end='')
        output.write()
        output.write(f"percent viewing algorithmic cells of their total number: {percent}", end='\n\n')
