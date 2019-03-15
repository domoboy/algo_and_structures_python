# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# сначала найдем минимумы и максимумы
# потом обменяем местами индексы

from random import random

# готовим массив
quantity = int(input('Укажите длину масссива: '))
data_array = [0] * quantity

for i in range(quantity):
    data_array[i] = int(random() * 100)

print(data_array)

# начинаем поиск минимумом и максимумов в массиве
minimal = min(data_array)
maximal = max(data_array)

# индекс минимального и максимального значений
index_minimal = data_array.index(minimal)
index_maximal = data_array.index(maximal)

print(f'Минимальное значение {minimal} на {index_minimal + 1} позиции')
print(f'Максимальное значение {maximal} на {index_maximal + 1} позиции')

# меняем местами
data_array[index_minimal], data_array[index_maximal] = data_array[index_maximal], data_array[index_minimal]

print(f'Новое значение массива: \n{data_array}')
