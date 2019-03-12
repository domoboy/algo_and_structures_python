"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

search_target = int(input('Какую цифру будем искать? '))
amount = int(input('Сколько чисел вы введете? '))

res = 0

print('Введите: ')

for el in range(1, amount + 1):
    number = int(input(str(el) + '-ое число: '))
    while number > 0:
        if number % 10 == search_target:
            res += 1
        number = number // 10

print(f'Число {search_target} встретилось - {res} раз/а')
