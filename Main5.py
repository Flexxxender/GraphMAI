from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task5 import Dijkstra

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(5)
    args = parser.args

    try:
        file_path, flag = parser.path_to_file, parser.input_flag

        if file_path:
            # вывод кратчайшего пути между вершинами
            graph = GraphModule.Graph(strategies[flag](file_path))
            output.check_file_needed(args.o)

            task5_graph = Dijkstra.GraphDijkstra(graph)
            distance, route = task5_graph.dijkstra(args.n, args.d)

            if distance == -2:
                output.write("Incorrect data")
            elif distance == -1:
                output.write(f"There is no path between the vertices {args.n + 1} and {args.d + 1}.")
            else:
                output.write(f"Shortest path length between {args.n + 1} and {args.d + 1} vertices: {distance}")
                output.write(f"Path: {route}")

        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
