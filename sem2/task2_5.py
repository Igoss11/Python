# Реализуйте алгоритм перемешивания списка.

start_list = list(range(-10, 10))
print(start_list)

for i in range(round(len(start_list)/2)):
    if i % 2 == 0:
        final_list = start_list[i]
        start_list[i] = start_list[- i]
        start_list[- i] = final_list
print(start_list)
