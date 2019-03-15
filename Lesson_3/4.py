# 4.	Определить, какое число в массиве встречается чаще всего.

from random import random

# готовим массив
quantity = int(input('Укажите длину масссива: '))
data_array = [0] * quantity

for i in range(quantity):
    data_array[i] = int(random() * 10)

print(data_array)

# начинаем перебирать значения сравнивая его с следующим
n = data_array[0]
number_repetitions = 1

for i in range(quantity - 1):

    number = 1

    for j in range(i + 1, quantity):
        if data_array[i] == data_array[j]:
            number += 1

    if number > number_repetitions:
        number_repetitions = number
        n = data_array[i]

# выводим количество повторений, либо сообщаем, что повторений нет
if number_repetitions > 1:
    print(f'Найдено число {n} - оно встречается {number_repetitions} раз(а)')
else:
    print('Повторений не встречено')

