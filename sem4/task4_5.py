# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy

x = sympy.symbols('x')

with open('file1.txt', 'r') as data:
    polynomial1 = data.read()
with open('file2.txt', 'r') as data:
    polynomial2 = data.read()

polynomial = (sympy.simplify((polynomial1 + '+' + polynomial2)))
print(polynomial1)
print(polynomial2)
print('Результирующий многочлен: ', polynomial)

with open("file_itog.txt", "w") as data:
    data.write("%s" % polynomial)
