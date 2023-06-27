import time
from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task4 import Kruskal, Prima, Boruvka

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    # словарь алгоритмов, где по ключу (флагу) получаем класс нужного алгоритма для графа
    algorithms = {
        'k': lambda graphh: Kruskal.AlgKruskal(graphh),
        'p': lambda graphh: Prima.AlgPrima(graphh),
        'b': lambda graphh: Boruvka.AlgBoruvka(graphh)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(4)
    args = parser.args

    try:
        file_path, input_flag, alg_flag = parser.path_to_file, parser.input_flag, parser.alg_flag

        if file_path:
            # вывод остовного дерева минимального веса графа
            graph = GraphModule.Graph(strategies[input_flag](file_path))
            output.check_file_needed(args.o)

            # если указаг флаг s - запускаем все алгоритмы поочередно
            if alg_flag == 's':
                for algorithm in algorithms.values():
                    task4_graph = algorithm(graph)

                    # подсчет времени для алгоритма
                    start = time.time()
                    tree, tree_weight = task4_graph.spanning_tree()
                    end = time.time() - start

                    output.write(f"Time spent by the {type(task4_graph).__name__}: {end}")
                    output.write(f"Minimum spanning tree:\n{tree}")
                    output.write(f"Weight of spanning tree: {tree_weight}\n")

            # иначе запускаем только один алгоритм и не считаем время
            else:
                task4_graph = algorithms[alg_flag](graph)
                tree, tree_weight = task4_graph.spanning_tree()
                output.write(f"Minimum spanning tree:\n{tree}")
                output.write(f"Weight of spanning tree: {tree_weight}")

        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
