import argparse

from task0 import Graph, Output, Strategy
from task5 import Dijkstra


# создание парсера, который будет считывать флаги исходного файла
# и также выходного, если потребуется
def create_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-e', default=False)
    argument_parser.add_argument('-m', default=False)
    argument_parser.add_argument('-l', default=False)
    argument_parser.add_argument('-o', default=False)

    argument_parser.add_argument('-n', required=True, type=int)
    argument_parser.add_argument('-d', required=True, type=int)

    return argument_parser


# проверка на то, что введен только один флаг из трех (-e, -m, -l)
def check_num_args(arguments):
    # считаем все ненулевые флаги и вычитаем флаг о, если тот был указан, а также флаги вершин
    count_flags = sum([1 for flag in vars(arguments).values() if flag is not False])
    count_flags -= (arguments.o is not False) + 2

    # если был указан один флаг, то находим флаг и с каким файлом он был указан
    if count_flags == 1:
        path_to_file = ''
        correct_flag = 0
        for i in vars(arguments):
            # нашли ненулевой флаг - запомнили его и имя файла
            if vars(arguments)[i] is not False:
                path_to_file = vars(arguments)[i]
                correct_flag = i
                break
        return path_to_file, correct_flag

    # иначе возвращаем ошибку
    return False, False


# проверка на нужду выходного файла
def check_file_needed(arg_o):
    if arg_o:
        # если файл нужен - меняем поток вывода из консоли на файл
        output.switch_to_file_output(arg_o)
        # очищаем файл путем открытия его для записи перед основной работой
        with open(arg_o, "w") as file:
            file.write("")


if __name__ == '__main__':
    # словарь стратегий, где по ключу (флагу) получаем функцию считывания матрицы из файла
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }


    output = Output.Output()  # создаем экземпляр класса Output из модуля Output
    parser = create_parser()  # создаем парсер
    args = parser.parse_args()  # получаем все флаги этого парсера

    path, flag = check_num_args(args)

    if (path, flag) != (False, False):

        graph = Graph.Graph(strategies[flag](path))
        check_file_needed(args.o)

        task5_graph = Dijkstra.GraphDijkstra(graph)
        distance, route = task5_graph.dijkstra(args.n, args.d)

        if distance == -2:
            output.write("Incorrect data")
        elif distance == -1:
            output.write(f"There is no path between the vertices {args.n + 1} and {args.d + 1}.")
        else:
            output.write(f"Shortest path length between {args.n + 1} and {args.d + 1} vertices: {distance}")
            output.write(f"Path: {route}")

    else:
        print("Было передано неверное количество ключей с параметрами")
