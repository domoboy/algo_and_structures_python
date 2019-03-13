"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
# складываем сумму в переменную
# само число от которой сумма складывать в другую
#
# циклом проверяем выше сумма или нет, и если да, то перезаписываем переменную
# с суммой и переменную хранящую число
# выводим самую большую сумму и у какого числа

highest_amount = 0
highest_number = 0

user_value = int(input('Введите число: '))

while user_value != 0:

    value = user_value
    sum = 0

    while user_value > 0:
        sum += value % 10
        user_value = user_value // 10

    if sum > highest_amount:
        highest_amount = sum
        highest_number = value

    user_value = int(input('Введите число: '))

# if user_value == '0':
#     print('Вы завершили программу:')
print(f'Число {highest_number}', end=' ')
print(f'имеет наибольшую сумму, она равна: {highest_amount}')
