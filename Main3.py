from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task3 import BridgesAndCutVertices

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(3)
    args = parser.args

    try:
        file_path, flag = parser.path_to_file, parser.input_flag

        if file_path:
            # вывод мостов и шарниров в графе
            graph = GraphModule.Graph(strategies[flag](file_path))
            output.check_file_needed(args.o)

            task3_graph = BridgesAndCutVertices.BridgesAndCutVertices(graph)

            output.write(f"Bridges: {task3_graph.bridges}")
            output.write(f"Cut vertices: {task3_graph.cut_vertices}")

        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
