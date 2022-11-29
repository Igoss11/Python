# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите координаты точки X: '))
y = int(input('Введите координаты точки Y: '))

if x > 0 and y > 0:
    print('Точка находится в 1 четверти')
elif x < 0 and y > 0:
    print('Точка находится в 2 четверти')
elif x < 0 and y < 0:
    print('Точка находится в 3 четверти')
elif x > 0 and y < 0:
    print('Точка находится в 4 четверти')
else:
    print('Неверный ввод данных')
