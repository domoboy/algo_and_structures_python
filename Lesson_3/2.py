"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import random

quantity = int(input('Укажите длину масссива: '))  # сколько значений

data_array = [0] * quantity  # создаю массив
even_list = []  # массив для записи четных

for i in range(quantity):
    data_array[i] = int(random() * 10) + 10  # заполняю первый массив случайными числами

    if data_array[i] % 2 == 0:  # проверяю четное ли
        even_list.append(i)  # добавляю во-второй массив

print(f'Для массива длиной {quantity}: {data_array}')
print(f'Индекс четных начиная с нуля: {even_list}')
