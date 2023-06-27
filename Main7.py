from task0 import ModifiedGraph, OutputModule, Strategy, ParserModule
from task7 import Johnson

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    # словарь стратегий, где по ключу (флагу) получаем функцию считывания матрицы из файла
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(7)
    args = parser.args

    try:
        file_path, flag = parser.path_to_file, parser.input_flag

        if file_path:
            # вывод кратчайших расстояний от всех вершин до всех
            output.check_file_needed(args.o)
            graph = ModifiedGraph.ModifiedGraph(strategies[flag](file_path))
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
