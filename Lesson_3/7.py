"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random

# готовим массив
quantity = int(input('Укажите длину масссива: '))
data_array = [0] * quantity

for i in range(quantity):
    data_array[i] = int(random() * 100)

print(data_array)

# определяем порядок первого минимума
if data_array[0] > data_array[1]:
    minimal_1 = 0
    minimal_2 = 1
else:
    minimal_1 = 1
    minimal_2 = 0

# в цикле перебираем значения
for i in range(2, quantity):

    if data_array[i] < data_array[minimal_1]:
        min_one = minimal_1
        minimal_1 = i

        if data_array[min_one] < data_array[minimal_2]:
            minimal_2 = min_one

    elif data_array[i] < data_array[minimal_2]:
        minimal_2 = i

print(f'Первое минимальное значение массива: {data_array[minimal_1]}')
print(f'Второе минимальное значение массива: {data_array[minimal_2]}')
