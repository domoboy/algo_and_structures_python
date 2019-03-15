# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

from random import random

# готовим массив
quantity = int(input('Укажите длину масссива: '))
data_array = []

for i in range(quantity):
    data_array.append(int(random() * 100) - 100)

print(data_array)

i = 0
max_negative = -1

while i < quantity:

    if data_array[i] < 0 and max_negative == -1:
        max_negative = i  # первый встретившийся отрицательный элемент

    elif data_array[i] < 0 and data_array[i] > data_array[max_negative]:
        max_negative = i

    i += 1

print(f'Макс. минимум равен {data_array[max_negative]} он на {max_negative + 1} месте в массиве')
