# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти: '))

if n == 1:
    print('В этой четверти x > 0 и y > 0')
elif n == 2:
    print('В этой четверти x < 0 и y > 0')
elif n == 3:
    print('В этой четверти x < 0 и y < 0')
elif n == 4:
    print('В этой четверти x > 0 и y < 0')
if n < 1 or n > 4:
    print('Неверный ввод данных')
