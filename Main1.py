import argparse
from task0 import Graph, Output, Strategy
from task1 import Task1


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
            # создаем граф через матрицу, полученную из стратегии, то есть
            # из словаря берется функция по флагу, которая считывает файл и
            # возвращает матрицу, которую мы передаем в конструктор класса граф
            # то есть сразу получаем готовый граф с нужной матрицей смежности
            graph = Graph.Graph(strategies[flag](path))

            # создаем экземпляр класса для первого задания, где в конструкторе
            # по нашему графу получаем матрицу достижимости, смежности, а также
            # сможем дальше работать по заданию с графом
            task1_graph = Task1.GraphFeatures(graph)
            task2_graph = Task1.GraphFeatures(graph)

            check_file_needed(args.o)

            # если граф ориентирован - считаем полустепени исхода и захода
            if task1_graph.is_directed:
                output.write(
                    f"deg+ = {task1_graph.vector_degrees()[0]}")
                output.write(
                    f"deg- = {task1_graph.vector_degrees()[1]}", end='\n\n')
            # иначе считаем просто степени
            else:
                output.write("deg =", task1_graph.vector_degrees(), end='\n\n')

            # вывод матрицы достижимости, эксцентриситетов, диаметра, радиуса,
            # центральных и периферийных вершин
            output.write("Distances:")
            output.write('\n'.join(map(str, task1_graph.distance_matrix())), end='\n\n')
            output.write(f"Eccentricity:\n{task1_graph.eccentricity()}")
            output.write(f"D = {task1_graph.diameter()}")
            output.write(f"R = {task1_graph.radius()}")
            output.write(f"Z = {task1_graph.central_vertices()}")
            output.write(f"P = {task1_graph.peripheral_vertices()}")

        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
