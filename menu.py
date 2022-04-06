# Скрипт для вывода сообщений пользователю.

from pprint import pprint
import input_data  # Скрипт для ввода данных


def print_database(database: dict):
    """
    Печатает базу данных.
    """
    pprint(database)


def get_menu_item() -> int:
    """
    Выводит меню и получает выбранный пункт.
    """
    menu_text = '\n~~~~~~~~~~~~~~~~~~~~~~~~~~ МЕНЮ ~~~~~~~~~~~~~~~~~~~~~~~~~~\n' \
                '1. Сформировать новую базу данных\n' \
                '2. Печать базы данных\n'\
                '3. \n' \
                '4. \n' \
                '5. \n' \
                '6. \n' \
                '7. \n' \
                '8. \n' \
                '0. Выход\n'

    print(menu_text)
    return input_data.get_int_number('Выберите пункт меню', 0)