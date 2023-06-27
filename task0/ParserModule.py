import argparse


class Parser:
    path_to_file = ""  # путь до входного файла
    input_flag = ""  # флаг, с которым входной файл задан
    alg_flag = ""  # флаг алгоритма который нужен в задании

    def __init__(self, task):
        self._argument_parser = None
        self._task = task
        # словарь парсеров для каждого задания, номер задания передается в конструктор
        # далее по номеру выбирается определенный парсер, по дефолту для всех остальных
        # заданий выбирается обычный парсер в случае 0
        _needed_parsers = {
            '0': lambda: self.classic_parser(),
            '4': lambda: self.task4_parser(),
            '5': lambda: self.task5_parser(),
            '6': lambda: self.task6_parser(),
            '8': lambda: self.task8_parser(),
            '9': lambda: self.task9_parser()
        }
        # устанавливаем дефолтное значение словаря, в случае, если номера таска нет в ключах
        _needed_parsers.setdefault(str(self._task), lambda: self.classic_parser())
        # вызываем метод для определенного таска в соответствии с номером задания
        _needed_parsers[str(self._task)]()

        self.checking_input_flags()

    # создание парсера, который будет считывать флаги исходного файла
    # -m матрица смежности, -e список ребер, -l список смежности
    # и также выходного, если потребуется (-o)
    def classic_parser(self):
        self._argument_parser = argparse.ArgumentParser()
        self._argument_parser.add_argument('-e', default=False)
        self._argument_parser.add_argument('-m', default=False)
        self._argument_parser.add_argument('-l', default=False)
        self._argument_parser.add_argument('-o', default=False)

    # получение парсера, чтобы получить его флаги
    @property
    def args(self):
        return self._argument_parser.parse_args()

    # добавляем флаги нужных алгоритмов для 4-го задания
    # -k Краскала, -b Борувки, -p Прима, -s все сразу с счетчиком времени
    def task4_parser(self):
        self.classic_parser()
        self._argument_parser.add_argument('-k', action='store_const', const=True, default=False)
        self._argument_parser.add_argument('-p', action='store_const', const=True, default=False)
        self._argument_parser.add_argument('-b', action='store_const', const=True, default=False)
        self._argument_parser.add_argument('-s', action='store_const', const=True, default=False)

        self.checking_alg_flags_4task()

    # -n начальная вершина, -d конечная вершина (откуда и до куда требуется найти путь)
    def task5_parser(self):
        self.classic_parser()
        self._argument_parser.add_argument('-n', required=True, type=int)
        self._argument_parser.add_argument('-d', required=True, type=int)

    # добавляем флаги алгоритмов и вершину, нужную для шестого задания
    # -d Дейкстры, -b Беллмана-Форда, -t Левита, -n вершина, от которой ищем все пути до остальных
    def task6_parser(self):
        self.classic_parser()
        self._argument_parser.add_argument('-d', action='store_const', const=True, default=False)
        self._argument_parser.add_argument('-b', action='store_const', const=True, default=False)
        self._argument_parser.add_argument('-t', action='store_const', const=True, default=False)
        self._argument_parser.add_argument('-n', required=True, type=int)

        self.checking_alg_flags_6task()

    # флаг -n, отвечающий за начальную вершину, откуда ищем гамильтонов цикл
    def task9_parser(self):
        self.classic_parser()
        self._argument_parser.add_argument('-n', required=True)

    # создание парсера, который будет считывать флаг исходного файла (только матрица)
    # выходного, если потребуется, и координаты начальной и конечной вершин (-n и -d)
    def task8_parser(self):
        self._argument_parser = argparse.ArgumentParser()
        self._argument_parser.add_argument('-m', required=True, default=False)
        self._argument_parser.add_argument('-o', default=False)
        self._argument_parser.add_argument('-n', required=True, nargs=2)
        self._argument_parser.add_argument('-d', required=True, nargs=2)

    # получение нужного флага входного файла и пути до этого файла
    # в случае, если подан не ровно один из флагов -e -m -l - ошибка
    def checking_input_flags(self):
        # если запускается 8-ое задание - пропускаем, там нужен только 1 флаг -m
        if self._task == 8:
            return
        # если на 4 или 6 задании на проверке флагов для алгоритмов уже нашли ошибку - пропускаем
        if self.path_to_file != "":
            return
        # получаем словарь из флагов и значений парсера
        parser_dict = vars(self._argument_parser.parse_args())
        count_flags = 0
        # идем по флагам и считаем кол-во не False значений в словаре
        for key in ["e", "m", "l"]:
            if parser_dict[key]:
                count_flags += 1
                self.path_to_file = parser_dict[key]
                self.input_flag = key
        if count_flags != 1:
            self.path_to_file = False
            self.input_flag = False

    # получение нужного флага алгоритма для 4 задания и проверка на что, что он один
    def checking_alg_flags_4task(self):
        # получаем словарь из флагов и значений парсера
        parser_dict = vars(self._argument_parser.parse_args())
        count_flags = 0
        # идем по флагам и считаем кол-во не False значений в словаре
        for key in ["k", "p", "b", "s"]:
            if parser_dict[key]:
                count_flags += 1
                self.alg_flag = key
        if count_flags != 1:
            self.alg_flag = False
            self.input_flag = False
            self.path_to_file = False

    # получение нужного флага алгоритма для 4 задания и проверка на что, что он один
    def checking_alg_flags_6task(self):
        # получаем словарь из флагов и значений парсера
        parser_dict = vars(self._argument_parser.parse_args())
        count_flags = 0
        # идем по флагам и считаем кол-во не False значений в словаре
        for key in ["d", "b", "t"]:
            if parser_dict[key]:
                count_flags += 1
                self.alg_flag = key
        if count_flags != 1:
            self.alg_flag = False
            self.input_flag = False
            self.path_to_file = False
