from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task10 import Flow

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    # словарь стратегий, где по ключу (флагу) получаем функцию считывания матрицы из файла
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(10)
    args = parser.args

    try:
        file_path, flag = parser.path_to_file, parser.input_flag

        if file_path:
            # вывод максимального потока в сети
            output.check_file_needed(args.o)
            graph = GraphModule.Graph(strategies[flag](file_path))
            task10_graph = Flow.FindMaxFlow(graph)

            if task10_graph.flow_matrix == -1:
                output.write("There is now sink or source")

            else:
                source = task10_graph.source
                sink = task10_graph.sink
                output.write(f"{task10_graph.max_flow} - maximum flow from {source + 1} to {sink + 1}.")

                for i in range(len(graph.adjacency_matrix())):
                    for j in range(len(graph.adjacency_matrix())):
                        if task10_graph.flow_matrix[i][j] != 1000000:
                            output.write(f"{i + 1} {j + 1} {task10_graph.flow_matrix[i][j]}/{graph.adjacency_matrix()[i][j]}")
        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
