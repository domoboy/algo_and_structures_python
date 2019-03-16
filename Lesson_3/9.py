# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

y = int(input('Сколько строк?: '))
x = int(input('Сколько элементов в строке?: '))

data_array = []
min_array = []

# создаем матрицу с пользовательскими парамметрами.
for i in range(y):
    row = []
    for j in range(x):
        n = int(random() * 100)
        row.append(n)
    print(row)

    data_array.append(row)
    min_array.append(min(row))

print(f'Массив минимальных значений матрицы: {min_array}')
print(f'Максимальный элемент среди минимальных в матрице: {max(min_array)}')
