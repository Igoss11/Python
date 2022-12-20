def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    telephone = input('Введите телефон: ')
    with open('Phonebook.txt', 'a', encoding='UTF - 8') as data:
        data.write(f'\n\n{surname} \n{name} \n{telephone}')


def export_contact():
    data_contact = []
    with open('Phonebook.txt', 'r', encoding='utf-8') as file:
        data_contact = file.read()
        list_contact = data_contact.split('\n')
    return list_contact


def search_contact():
    data = export_contact()
    data_list = []
    val = 1
    word = input('Введите имя или фамилию: ')
    for line in data:
        if word in line:
            val = 0
            data_list.append(line)
    if val:
        print('Такого контакта нет!')
    return data_list


def delete_contact():
    data = export_contact()
    find = search_contact()
    if find != []:
        if len(find) == 1:
            for i in range(len(data) - 1):
                if data[i] == find[0]:
                    data.pop(i)
                    new_str = "\n\n".join(data)
                    with open('Phonebook.txt', 'w', encoding='utf-8') as file:
                        file.write(new_str)
                        break
    else:
        print('Контакт не найден!')


print(delete_contact())
