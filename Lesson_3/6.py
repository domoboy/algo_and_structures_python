"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random

# готовим массив
quantity = int(input('Укажите длину масссива: '))
data_array = [0] * quantity

for i in range(quantity):
    data_array[i] = int(random() * 100)

print(data_array)

# найдем индексы максимального и минимального значения массива
maximal = 0
minimal = 0

for i in range(1, quantity):
    if data_array[i] < data_array[minimal]:
        minimal = i
    elif data_array[i] > data_array[maximal]:
        maximal = i

print(f'Максимальное значение: {data_array[maximal]} \nМинимальное значение: {data_array[minimal]}')

# проверяем не находится ли минимум "выше" по массиву, если выше переворачиваем значения
if minimal > maximal:
    maximal, minimal = minimal, maximal

# находим сумму элементов между минимальным и максимальным значениями
sum_array = 0

for i in range(minimal + 1, maximal):
    sum_array += data_array[i]

# если расстояния между минимальным и максимальным нет
if sum_array == 0:
    print('Нет чисел, которые можно было бы сложить по условию задачи')
else:
    print(f'Сумма элементов между максимальным и минимальным значением составляет: {sum_array}')
