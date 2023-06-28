# Алгоритмы и задачи теории графов - GraphMAI


## В данном проекте реализованы следующие алгоритмы и задачи теории графов:
1. Программа, рассчитывающая следующие характеристики графа/орграфа:
вектор степеней вершин, матрицу расстояний, диаметр, радиус,
множество центральных вершин (для графа), множество периферийных
вершин (для графа). ```Алгоритм Флойда-Уоршелла```

2. Программа, определяющая связность. Для графа – связность, а также
количество и состав компонент связности. Для орграфа – сильную, слабую
связность, или несвязность. А также количество и состав компонент
связности и сильной связности. ```BFS - алгоритм поиска в ширину```

3. Программа, находящая мосты и шарниры в графе. ```DFS - алгоритм поиска в глубину```

4. Программа, находящая остовное дерево графа. Для орграфа находится
остовное дерево соотнесённого графа. ```Алгоритмы Борувки, Краскала, Прима```

5. Программа, находящая геодезическую цепь между двумя вершинами в
графе. ```Алгоритм Дейкстры```

6. Программа, рассчитывающая расстояние от указанной вершины до всех
остальных вершин в графе. ```Алгоритмы Дейкстры, Беллмана-Форда-Мура, Левита```

7. Программа, рассчитывающая расстояние между всеми парами вершин в
графе. ```Алгоритм Джонсона```

8. Программа, рассчитывающая расстояние между двумя точками на карте. ```Алгоритм А*```

9. Программа, находящая гамильтонов путь в графе. ```Метод муравьиной колонии```

10. Программа, рассчитывающая максимальный поток в сети. ```Алгоритм Эдмондса-Карпа```

11. Программа, находящая максимальные паросочетания. Перед этим
определяется, является ли граф двудольным. ```Алгоритм Эдмондса-Карпа с добавлением двух вершин```

___

## Требования к входным файлам:

1. Граф, заданный ```списком рёбер```. Каждое ребро хранится отдельной
строкой. В строке три числа, разделённых пробелом: исходящая
вершина, входящая вершина, вес ребра. Номера вершин представляют
собой натуральные числа с нулём. Размерность графа определяется
автоматически (от 0 вершины до вершины с наибольшим номером).

2. Граф, заданный ```списками смежности```. Номер строки представляет собой
номер вершины графа, в строке через пробел перечислены номера
смежных вершин.

3. Граф, заданный ```матрицей смежности```. Значения в строках разделены
пробелами.

4. (Для **8** задания) ```Карта```, представляющая собой прямоугольную матрицу, где 𝑖-я строка и
𝑗-й столбец задают «клетку» на карте. Значение представляет собой
высоту местности в данной точке. Переход возможен только между
соседними «клетками» по вертикали или горизонтали.

___

## Запуск задания
Запуск заданий происходит через консоль, например, для большинства заданий строка должна выглядеть так:
```
python Main1.py -m task1/matrices/matrix_t1_001.txt -o output.txt
```

#### Основные флаги для работы с заданиями
После всех этих флагов должен идти путь к файлу, привем только один и только один из флагов ```-e```, ```-m```, ```-l``` может быть подан на вход программмы
``` 
-m - флаг входного файла, который задан в виде матрицы смежности
-e - флаг входного файла, который задан в виде списка рёбер
-l - флаг входного файла, который задан в виде списков смежности
-o - флаг выходного файла (при необходимости, иначе вывод результата будет произведен в консоль)
```
> Будьте внимательны, если вы перепутаете флаги входного файла и запустите программу, будет выдан некорректный результат

#### Дополнительные флаги для работы с заданиями
Также в некоторых заданиях должны быть дополнительные флаги, для каждого отдельного задания будет свой readme.md, в котором это будет показано