from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task2 import DirectedGraph, UndirectedGraph

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    strategies = {
        'm': lambda path: Strategy.matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(2)
    args = parser.args

    try:
        file_path, flag = parser.path_to_file, parser.input_flag

        if file_path:
            # вывод сильных/слабых компонент связности графа
            graph = GraphModule.Graph(strategies[flag](file_path))
            output.check_file_needed(args.o)

            # если граф ориентирован - нужен Косараджу
            if graph.is_directed():
                task2_graph = DirectedGraph.DirectedGraph(graph)
                kosaraju = task2_graph.kosaraju()

                if kosaraju[0] == 1:
                    output.write("Graph is strongly connected")
                elif task2_graph.is_graph_weak_connected():
                    output.write("Graph is weakly connected")
                else:
                    output.write("Graph is not connected")

                output.write(f"{kosaraju[0]} Strongly connected components:\n{kosaraju[1]}")
                output.write(f"{task2_graph.count_weak_connected_components()[0]} Weakly connected components:\n\
{task2_graph.count_weak_connected_components()[1]}")

            # если граф не ориентирован
            else:
                # выписываем связный он или нет и компоненты связности
                task2_graph = UndirectedGraph.UndirectedGraph(graph)
                if task2_graph.is_graph_connected():
                    output.write("Graph is connected")
                else:
                    output.write("Graph is not connected")
                output.write(f"{task2_graph.count_graph_connected_components()[0]} Connected components:\n\
{task2_graph.count_graph_connected_components()[1]}")

        else:
            print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    except Exception as e:
        print(e)
