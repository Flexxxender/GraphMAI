import argparse
from task0 import Graph, Output, Strategy
from task10 import Flow


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

    # если указано верное количество флагов - действуем
    path, flag = check_num_args(args)

    if (path, flag) != (False, False):
        check_file_needed(args.o)
        graph = Graph.Graph(strategies[flag](path))
        task10_graph = Flow.FindMaxFlow(graph)

        if task10_graph.flow_matrix == -1:
            output.write("There is now sink or source")

        source = task10_graph.source
        sink = task10_graph.sink
        output.write(f"{task10_graph.max_flow} - maximum flow from {source + 1} to {sink + 1}.")
        for i in range(len(graph.adjacency_matrix())):
            for j in range(len(graph.adjacency_matrix())):
                if task10_graph.flow_matrix[i][j] != 1000000:
                    output.write(f"{i + 1} {j + 1} {task10_graph.flow_matrix[i][j]}/{graph.adjacency_matrix()[i][j]}")

    else:
        print("Было передано неверное количество ключей с параметрами")
