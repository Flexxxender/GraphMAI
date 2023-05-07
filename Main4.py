import argparse
import time

from task0 import Graph, Output, Strategy
from task4 import Kruskal, Prima, Boruvka


# создание парсера, который будет считывать флаги исходного файла и алгоритмов
# и также выходного файла, если потребуется
def create_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-e', default=False)
    argument_parser.add_argument('-m', default=False)
    argument_parser.add_argument('-l', default=False)
    argument_parser.add_argument('-o', default=False)


    argument_parser.add_argument('-k', action='store_const', const=True, default=False)
    argument_parser.add_argument('-p', action='store_const', const=True, default=False)
    argument_parser.add_argument('-b', action='store_const', const=True, default=False)
    argument_parser.add_argument('-s', action='store_const', const=True, default=False)

    return argument_parser


# проверка количества аргументов
def check_num_args(arguments):
    count_input_flags = (arguments.e is not False) + (arguments.m is not False) + \
                        (arguments.l is not False)

    count_alg_flags = (arguments.k is not False) + (arguments.p is not False) + \
                      (arguments.b is not False) + (arguments.s is not False)

    # проверили, что введен 1 флаг входного файла и 1 флаг алгоритма - находим их
    if count_input_flags == 1 and count_alg_flags == 1:
        path_to_file = ''
        correct_input_flag = 0
        correct_alg_flag = 0
        for i in vars(arguments):
            if vars(arguments)[i] is not False and i in ["e", "m", "l"]:
                path_to_file = vars(arguments)[i]
                correct_input_flag = i
            elif vars(arguments)[i] is not False and i in ["k", "p", "b", "s"]:
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
        'k': lambda graph: Kruskal.AlgKruskal(graph),
        'p': lambda graph: Prima.AlgPrima(graph),
        'b': lambda graph: Boruvka.AlgBoruvka(graph)
    }

    output = Output.Output()  # создаем экземпляр класса Output из модуля Output
    parser = create_parser()  # создаем парсер
    args = parser.parse_args()  # получаем все флаги этого парсера

    path, input_flag, alg_flag = check_num_args(args)

    if path is not False:

        graph = Graph.Graph(strategies[input_flag](path))
        check_file_needed(args.o)

        # если указаг флаг s - запускаем все алгоритмы поочередно
        if alg_flag == 's':
            for algorithm in algorithms.values():
                task4_graph = algorithm(graph)

                # подсчет времени для алгоритма 
                start = time.time()
                tree, tree_weight = task4_graph.spanning_tree()
                end = time.time() - start

                output.write(f"Time spent by the {type(task4_graph).__name__}: {end}")
                output.write(f"Minimum spanning tree:\n{tree}")
                output.write(f"Weight of spanning tree: {tree_weight}\n")

        # иначе запускаем только один алгоритм и не считаем время
        else:
            task4_graph = algorithms[alg_flag](graph)
            tree, tree_weight = task4_graph.spanning_tree()
            output.write(f"Minimum spanning tree:\n{tree}")
            output.write(f"Weight of spanning tree: {tree_weight}")

    else:
        print("Было передано неверное количество ключей с параметрами")
