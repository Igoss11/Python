# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.(записать в строку)

from random import randint

k = int(input('Введите натуральную степень k: '))
polynomial = ''
degree = k

while degree >= 0:
    num = randint(0, 100)
    if degree > 1:
        polynomial += f'{num}x^{degree}'
    elif degree == 1:
        polynomial += f'{num}x'
    elif degree == 0:
        polynomial += f'{num} = 0'
    if degree > 0:
        polynomial += ' + '
    degree -= 1

f = open('file.txt', 'w')
f.write(str(polynomial))
f.close()
