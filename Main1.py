from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task1 import Task1

if __name__ == '__main__':
    # словарь стратегий, где по ключу (флагу) получаем функцию считывания матрицы из файла
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()  # создаем экземпляр класса Output из модуля Output
    parser = ParserModule.Parser(1)  # создаем парсер
    args = parser.args  # получаем все флаги этого парсера

    try:
        # если указано верное количество флагов - действуем
        file_path, flag = parser.path_to_file, parser.input_flag

        if file_path:
            # создаем граф через матрицу, полученную из стратегии
            graph = GraphModule.Graph(strategies[flag](file_path))
            # создаем экземпляр класса для первого задания
            task1_graph = Task1.GraphFeatures(graph)
            # проверка на нужду файла
            output.check_file_needed(args.o)

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
