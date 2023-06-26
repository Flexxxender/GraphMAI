import argparse
from task0 import Graph, Output, Strategy
from task9 import AntColony


# создание парсера, который будет считывать флаги исходного файла
# и также выходного, если потребуется
def create_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-e', default=False)
    argument_parser.add_argument('-m', default=False)
    argument_parser.add_argument('-l', default=False)
    argument_parser.add_argument('-o', default=False)

    argument_parser.add_argument('-n')

    return argument_parser


# проверка на то, что введен только один флаг из трех (-e, -m, -l)
def check_num_args(arguments):
    # считаем все ненулевые флаги и вычитаем флаг о, если тот был указан
    count_flags = (arguments.e is not False) + (arguments.m is not False) + \
                  (arguments.l is not False)

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
        'm': lambda path: Strategy.a_star_matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = Output.Output()  # создаем экземпляр класса Output из модуля Output
    parser = create_parser()  # создаем парсер
    args = parser.parse_args()  # получаем все флаги этого парсера

    # если указано верное количество флагов - действуем
    path, flag = check_num_args(args)

    if (path, flag) != (False, False):
        check_file_needed(args.o)
        graph = Graph.Graph(strategies[flag](path))
        task9_graph = AntColony.AntColony(graph)
        res = task9_graph.ant_colony(int(args.n))

        len = sum(res[i][2] for i in range(len(res)))
        output.write(f"Hamiltonian cycle has length {len}.")
        for i in res:
            output.write(f"{i[0] + 1} - {i[1] + 1} : ({i[2]})")

    else:
        print("Было передано неверное количество ключей с параметрами")
