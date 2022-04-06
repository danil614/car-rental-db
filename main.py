# Вариант 10. Аренда автомобилей.

from create_database import fill_database  # Скрипт для заполнения базы данных случайными значениями
import input_data  # Скрипт для ввода данных
import json_files  # Скрипт для работы с json файлами
import menu  # Скрипт для вывода сообщений


def load_database_from_file():
    """
    Загружает базу данных из json файла и проверяет ее.
    """
    message = ''
    data = json_files.get_data_from_json()

    if len(data) == 0:
        message = 'При загрузке возникла ошибка!\n' \
                  'База данных пустая или файл не найден.'

    print(message)

    return data


def check_database_structure(database: dict):
    messages = []
    is_correct = True

    if database.get('Автомобили') is None:
        is_correct = False
        messages.append('Ключ "Автомобили" не существует')
    else:
        cars = database['Автомобили']

        if not isinstance(cars, list):
            is_correct = False
            messages.append('Значение по ключу "Автомобили" не содержит список')

    if database.get('Водители') is None:
        is_correct = False
        messages.append('Ключ "Водители" не существует')
    else:
        drivers = database['Водители']

        if not isinstance(drivers, list):
            is_correct = False
            messages.append('Значение по ключу "Водители" не содержит список')

    return is_correct, messages


def main():
    database = {}

    while True:
        match menu.get_menu_item():
            case 0:  # Выход
                break
            case 1:  # Сформировать новую базу данных
                database = fill_database()
            case 2:  # Печать базы данных
                menu.print_database(database)
            case 3:  #
                pass
            case 4:  #
                pass
            case 5:  #
                pass
            case 6:  #
                pass
            case 7:  #
                pass
            case 8:  #
                pass
            case _:
                print('Неправильно введен номер пункта меню!')


if __name__ == '__main__':
    main()
