# Найти сумму и произведение цифр трехзначного числа введенного пользователем

user_number = input('Введите трехзначное число: ')

multiplication_of_number = 1
sum_of_numbers = 0

for el in user_number:
    multiplication_of_number *= int(el)
    sum_of_numbers += int(el)

print(multiplication_of_number)
print(sum_of_numbers)
