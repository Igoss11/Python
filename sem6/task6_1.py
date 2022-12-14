# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate,
# list comprehension. 3 любых задания(из любого урока)

# Задача 1 из семинара №3.

# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [2, 3, 5, 9, 3]
sum = 0

for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]

print(f'Сумма элементов на нечётной позиции = {sum}')


# Новое решение c map и enumerate:


result = list(map(int, [2, 3, 5, 9, 3]))
print(list(enumerate(result)))
sum = 0
for i in range(len(result)):
    if i % 2 != 0:
        sum += result[i]
print(f'Сумма элементов на нечётной позиции = : {sum}')
