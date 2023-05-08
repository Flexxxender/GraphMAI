import argparse

from task0 import Graph, Output, Strategy
from task6 import Dijkstra, BellmanFord, Levit


# создание парсера, который будет считывать флаги исходного файла
# и также выходного, если потребуется
def create_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-e', default=False)
    argument_parser.add_argument('-m', default=False)
    argument_parser.add_argument('-l', default=False)
    argument_parser.add_argument('-o', default=False)

    argument_parser.add_argument('-d', action='store_const', const=True, default=False)
    argument_parser.add_argument('-b', action='store_const', const=True, default=False)
    argument_parser.add_argument('-t', action='store_const', const=True, default=False)

    argument_parser.add_argument('-n', required=True, type=int)

    return argument_parser


# проверка количества аргументов
def check_num_args(arguments):
    count_input_flags = (arguments.e is not False) + (arguments.m is not False) + \
                        (arguments.l is not False)

    count_alg_flags = (arguments.d is not False) + (arguments.t is not False) + \
                      (arguments.b is not False)

    # проверили, что введен 1 флаг входного файла и 1 флаг алгоритма - находим их
    if count_input_flags == 1 and count_alg_flags == 1:
        path_to_file = ''
        correct_input_flag = 0
        correct_alg_flag = 0
        for i in vars(arguments):
            if vars(arguments)[i] is not False and i in ["e", "m", "l"]:
                path_to_file = vars(arguments)[i]
                correct_input_flag = i
            elif vars(arguments)[i] is not False and i in ["d", "t", "b"]:
                correct_alg_flag = i
        return path_to_file, correct_input_flag, correct_alg_flag

    # иначе возвращаем ошибку
    return False, False, False


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

    # словарь алгоритмов, где по ключу (флагу) получаем класс нужного алгоритма для графа
    algorithms = {
        'd': lambda graph, arg: Dijkstra.AlgDijkstra(graph, arg),
        't': lambda graph, arg: Levit.AlgLevit(graph, arg),
        'b': lambda graph, arg: BellmanFord.AlgBellmanFord(graph, arg)
    }

    output = Output.Output()  # создаем экземпляр класса Output из модуля Output
    parser = create_parser()  # создаем парсер
    args = parser.parse_args()  # получаем все флаги этого парсера

    path, input_flag, alg_flag = check_num_args(args)

    if path is not False:

        graph = Graph.Graph(strategies[input_flag](path))
        check_file_needed(args.o)
        task6_graph = algorithms[alg_flag](graph, args.n)

        if task6_graph.distance == -10:
            output.write(f"Graph contains a negative cycle.")
        else:
            output.write("Graph does not contain edges with negative weight")
            output.write("Shortest paths lengths:")

            for index, distance in enumerate(task6_graph.distance):
                if index != args.n:
                    output.write(f"{args.n + 1} - {index + 1}: {distance if distance != 1000000 else 'inf'}")

    else:
        print("Было передано неверное количество ключей с параметрами")
