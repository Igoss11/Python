# Задача 3 из семинара №4.

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.

import random

list = [random.randint(-10, 10) for i in range(10)]
print('Последовательность чисел:', *list)

list2 = []
for i in list:
    if list.count(i) == 1:
        list2.append(i)

print('Список неповторяющихся элементов:', list2)


# Новое решение c List Comprehension:


list = [random.randint(-10, 10) for i in range(10)]
print('Последовательность чисел:', *list)

list2 = [i for i in list if not list.count(i) >= 2]

print('Список неповторяющихся элементов:', list2)
