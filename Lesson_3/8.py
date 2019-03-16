"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки..
В конце следует вывести полученную матрицу.
"""
x = 5
y = 4

data_array = []

for i in range(y):
    row = []
    sum_array = 0
    print(f'Заполняем данные для строки №: {i + 1}')

    for j in range(x - 1):
        num = int(input(f'{j + 1}: '))
        sum_array += num
        row.append(num)

    row.append(sum_array)
    data_array.append(row)

for i in data_array:
    print(i)
