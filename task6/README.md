## 6 задание

Программа, рассчитывающая расстояние от указанной вершины до всех
остальных вершин в графе. Результатом работы является перечисление
пар вершин, и соответствующих расстояний между ними.

Входные данные для работы программы задаются следующими ключами
с параметрами:

```powershell
-e "edges_list_file_path"
-m "adjacency_matrix_file_path"
-l "adjacency_list_file_path"
```

Одновременно может указываться только один из этих ключей. Если
указано более одного – выдается сообщение об ошибке.

Алгоритм для расчёта задаётся следующими ключами:

```
-d – алгоритм Дейкстры
-b – алгоритм Беллмана-Форда-Мура
-t – алгоритм Левита
```

Если граф/орграф не удовлетворяет требованиям алгоритма к входным
данным, выдается соответствующее предупреждение.

Начальная вершина задаётся следующим ключом:
```powershell
-n begin_vertex_number
```
Данный ключ является **обязательным**.

Результаты работы выводятся на экран, либо в файл при указании
следующего ключа: ```-o "output_file_path"```

___
### Как должна выглядеть командная строка
```powershell
python Main6.py -m task6/matrices/matrix_t6_001.txt -o output.txt -n 5 -d 
```