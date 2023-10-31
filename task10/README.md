## 10 задание

Программа, рассчитывающая максимальный поток в сети. Расчёт
выполняется алгоритмом Эдмондса-Карпа. Источник и сток
определяются автоматически. Результатом работы является список рёбер
с указанием величины потока.


Входные данные для работы программы задаются следующими ключами
с параметрами:

```powershell
-e "edges_list_file_path"
-m "adjacency_matrix_file_path"
-l "adjacency_list_file_path"
```

Одновременно может указываться только один из этих ключей. Если
указано более одного – выдается сообщение об ошибке.

Результаты работы выводятся на экран, либо в файл при указании
следующего ключа: ```-o "output_file_path"```

___
### Как должна выглядеть командная строка
```powershell
python Main10.py -m task10/matrices/matrix_t10_001.txt -o output.txt 
```