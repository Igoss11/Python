# Задайте список из n чисел последовательности
# (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
sum = 0
list = [round(((1 + 1/i)**i), 2) for i in range(1, n+1)]

for i in list:
    sum += i
print(f'Cумма элементов: {sum}')
