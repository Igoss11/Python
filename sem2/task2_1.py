# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

num = float(input('Введите число: '))
sum = 0
for i in str(num):
    if i != ".":
        sum += int(i)
print(f'Сумма цифр: {sum}')
