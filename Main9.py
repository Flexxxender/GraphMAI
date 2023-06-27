from task0 import GraphModule, OutputModule, Strategy, ParserModule
from task9 import AntColony

# все комментарии по коду есть в Main1.py, они одинаковы
if __name__ == '__main__':
    # словарь стратегий, где по ключу (флагу) получаем функцию считывания матрицы из файла
    strategies = {
        'm': lambda path: Strategy.a_star_matrix_strategy(path),
        'e': lambda path: Strategy.edges_strategy(path),
        'l': lambda path: Strategy.list_strategy(path)
    }

    output = OutputModule.Output()
    parser = ParserModule.Parser(9)
    args = parser.args

    #try:
    file_path, flag = parser.path_to_file, parser.input_flag

    if file_path:
        # вывод гамильтонового цикла и его длины
        output.check_file_needed(args.o)
        graph = GraphModule.Graph(strategies[flag](file_path))
        task9_graph = AntColony.AntColony(graph)
        res = task9_graph.ant_colony(int(args.n))

        length = sum(res[i][2] for i in range(len(res)))
        output.write(f"Hamiltonian cycle has length {length}.")
        for i in res:
            output.write(f"{i[0] + 1} - {i[1] + 1} : ({i[2]})")

    else:
        print("Было передано неверное количество ключей с параметрами")
    # если получаем хоть одну ошибку - кидаем исключение
    #except Exception as e:
    #    print(e)
