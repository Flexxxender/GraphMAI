from task0 import ModifiedGraph, OutputModule, Strategy, ParserModule
from task11 import Matching

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    # словарь стратегий, где по ключу (флагу) получаем функцию считывания матрицы из файла
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(11)
    args = parser.args

    try:
        file_path, flag = parser.path_to_file, parser.input_flag

        if file_path:
            # вывод максимального паросочетания в двудольном графе
            output.check_file_needed(args.o)
            graph = ModifiedGraph.ModifiedGraph(strategies[flag](file_path))
            task11_graph = Matching.Matching(graph)

            matching = task11_graph.find_max_matching()
            if matching == -1:
                output.write("Graph is not bipartite")
            else:
                output.write("Graph is bipartite")
                output.write("Matching:")
                for i in range(len(matching)):
                    for j in range(len(matching)):
                        if matching[i][j] == 1:
                            output.write(f"{i + 1} - {j + 1}")
        else:
            print("Было передано неверное количество ключей с параметрами")
    # все комментарии по коду есть в Main1.py, они одинаковы
    except Exception as e:
        print(e)
