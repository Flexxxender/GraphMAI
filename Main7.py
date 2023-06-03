import argparse
from task0 import ModifiedGraph, Output, Strategy
from task7 import Johnson


# создание парсера, который будет считывать флаги исходного файла
# и также выходного, если потребуется
def create_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-e', default=False)
    argument_parser.add_argument('-m', default=False)
    argument_parser.add_argument('-l', default=False)
    argument_parser.add_argument('-o', default=False)

    return argument_parser


# проверка на то, что введен только один флаг из трех (-e, -m, -l)
def check_num_args(arguments):
    # считаем все ненулевые флаги и вычитаем флаг о, если тот был указан
    count_flags = sum([1 for flag in vars(arguments).values() if flag is not False])
    count_flags -= arguments.o is not False

    # если был указан один флаг, то находим флаг и с каким файлом он был указан
    if count_flags == 1:
        path_to_file = ''
        correct_flag = 0
        for i in vars(arguments):
            # нашли ненулевой флаг - запомнили его и имя файла
            if vars(args)[i] is not False:
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

    try:
        # если указано верное количество флагов - действуем
        path, flag = check_num_args(args)

        if (path, flag) != (False, False):
            check_file_needed(args.o)
            graph = ModifiedGraph.ModifiedGraph(strategies[flag](path))
            task7_graph = Johnson.AlgJohnson(graph)

            if task7_graph.distances == -10:
                output.write("Graph contains a negative cycle.")
            else:
                if task7_graph.negative_edge:
                    output.write("Graph contains edges with negative weight.")
                else:
                    output.write("Graph does not contain edges with negative weight.")

                output.write("Shortest paths lengths:")
                for i in range(len(task7_graph.distances)):
                    for j in range(len(task7_graph.distances)):
                        if task7_graph.distances[i][j] != 1000000 and i != j:
                            output.write(f"{i + 1} - {j + 1}: {task7_graph.distances[i][j]}")
        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
