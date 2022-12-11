# Создайте программу для игры в ""Крестики-нолики""
# (в консоли происходит выбор позиции)


def show_field(field: list):
    for i in range(3):
        print(field[0 + i * 3], '|',
              field[1 + i * 3], '|',
              field[2 + i * 3],)


def new_field(field: list, player: str):
    show_field(field)
    x = int(input(f'Select your button {player}: '))
    if x > 0 or x < 10:
        if str(field[x - 1]) in 'XO':
            print('Select another button')
        else:
            field[x - 1] = player
            return


def win(field: list):
    board = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in board:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return True
    return False


def game():
    field = [i for i in range(1, 10)]
    count = 0
    check = False
    while not check:
        if count % 2 == 0:
            new_field(field, 'X')
        else:
            new_field(field, 'O')
        count += 1
        if count > 3:
            check = win(field)
            if check:
                print('Win!')
                show_field(field)
                return
        if count == 9:
            print('Draw')
            show_field(field)
            return


game()
