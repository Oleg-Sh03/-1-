# Найдите сумму цифр трехзначного числа.
print("Введите трехзначное число:")
number = int(input())
if (number >= 100 and number <= 999):
    print((number % 10) + ((number - (number % 10)) // 10 - (number // 100) * 10) + number // 100)
else:
    print("Ошибка ввода") 