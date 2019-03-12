"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""
# вычислим левую и правую части и сравним, если равны, то равенство выполняется
n = int(input('n = '))

list = range(1, n + 1)

def rec_sum(s):
    if len(s) == 0:
        return 0
    else:
        return rec_sum(s[:-1]) + s[-1]

left_side = rec_sum(list)
right_side = n * (n + 1) / 2

if left_side == int(right_side):
    print('Равенство выполняется!')

print(f'{left_side} = {int(right_side)}')
