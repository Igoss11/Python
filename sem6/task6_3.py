# Задача 3 из семинара №3.

# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

list = [1.1, 1.2, 3.1, 5, 10.01]
min = 0
max = 0

for i in list:
    if i % 1 > max:
        max = i % 1
    else:
        min = i % 1

print('Разница между max и min значением = ', round(max - min, 2))


# Новое решение с lambda, map и filter:


list1 = [1.1, 1.2, 3.1, 5, 10.01]


def task(list1):
    num_map = map(lambda i: i % 1, list1)
    num_list = list(filter(lambda x: x != 0, num_map))
    num_min = min(num_list)
    num_max = max(num_list)
    return round(num_max - num_min, 2)


list2 = [1.1, 1.2, 3.1, 5, 10.01]
print(task(list2))
