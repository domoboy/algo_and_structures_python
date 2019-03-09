# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.
num_a = 5
num_b = 6

print(f'Число {num_a} в битовом представлении {bin(num_a)}')
print(f'Число {num_b} в битовом представлении {bin(num_b)}')

print(f'{num_a} AND {num_b} = {num_a & num_b} в битовом: {bin(num_a & num_b)}')
print(f'{num_a} OR {num_b} = {num_a | num_b} в битовом: {bin(num_a | num_b)}')
print(f'{num_a} XOR {num_b} = {num_a ^ num_b} в битовом: {bin(num_a ^ num_b)}')

print(f'Сдвиг {num_a} вправо на два знака = {num_a >> 2} ({bin(num_a >> 2)})')
print(f'Сдвиг {num_a} влево на два знака = {num_a << 2} ({bin(num_a << 2)})')
