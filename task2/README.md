## 2 задание

Программа, определяющая связность. Для графа – связность, а также
количество и состав компонент связности. Для орграфа – сильную, слабую
связность, или несвязность. А также количество и состав компонент
связности и сильной связности. Для определения используется поиск в
ширину.

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
python Main2.py -m task2/matrices/matrix_t2_001.txt -o output.txt 
```
