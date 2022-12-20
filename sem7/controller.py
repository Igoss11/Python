import view
import logger


def run():
    menu_item = view.menu()
    if menu_item == '1':
        logger.add_contact()
    elif menu_item == '2':
        print(logger.search_contact())
    else:
        print('Введите 1 или 2')
