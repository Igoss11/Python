# Вычислить число Пи c заданной точностью d

from math import pi

n = int(input('Введите заданную точность: '))
print(f'Число Пи: {round(pi, n)}')
