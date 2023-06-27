from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task6 import Dijkstra, BellmanFord, Levit

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    # словарь стратегий, где по ключу (флагу) получаем функцию считывания матрицы из файла
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    # словарь алгоритмов, где по ключу (флагу) получаем класс нужного алгоритма для графа
    algorithms = {
        'd': lambda graphh: Dijkstra.AlgDijkstra(graphh),
        't': lambda graphh: Levit.AlgLevit(graphh),
        'b': lambda graphh: BellmanFord.AlgBellmanFord(graphh)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(6)
    args = parser.args

    try:
        file_path, input_flag, alg_flag = parser.path_to_file, parser.input_flag, parser.alg_flag

        if file_path:
            # вывод кратчайший расстояний от одной вершины до остальных
            graph = GraphModule.Graph(strategies[input_flag](file_path))
            output.check_file_needed(args.o)
            task6_graph = algorithms[alg_flag](graph)
            distances = task6_graph.distances(args.n)

            if distances == -1:
                output.write("Incorrect data")
            elif distances == -10:
                output.write("Graph contains a negative cycle.")
            else:
                output.write("Graph does not contain edges with negative weight")
                output.write("Shortest paths lengths:")

                for index, distance in enumerate(distances):
                    if index != args.n:
                        output.write(f"{args.n + 1} - {index + 1}: {distance if distance != 1000000 else 'inf'}")

        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
