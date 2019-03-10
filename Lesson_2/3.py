"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
num = int(input('Введите число: '))

def inverted_number(n):
    if n < 10:  # базовый случай, если введена число из одной цифры
        print(int(n), end='')
        return n
    else:
        print(int(n) % 10, end='')
        return inverted_number(n / 10)

inverted_number(num)
print()

# Для проверки
# inverted_number(3486)
# print()
