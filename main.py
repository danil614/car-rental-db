# Вариант 10. Аренда автомобилей.
import create_elements
from create_elements import fill_database  # Скрипт для заполнения базы данных случайными значениями
import input_data  # Скрипт для ввода данных
import json_files  # Скрипт для работы с json файлами
import menu  # Скрипт для вывода сообщений
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи

def download_database_from_file() -> dict:
    """
    Загружает базу данных из json файла.
    """
    data = json_files.get_data_from_json()

    if len(data) == 0:
        message = 'При загрузке возникла ошибка!\n' \
                  'База данных пустая или файл не найден.'
    else:
        message = 'База данных успешно загружена из файла!'

    print(message)
    return data


def save_database_to_file(database: dict):
    """
    Сохраняет базу данных в json файл.
    """
    if not json_files.save_json_file(database):
        message = '\nПри сохранении базы данных в файл произошла ошибка!'
    else:
        message = '\nБаза данных успешно сохранена в файл!'
    print(message)


def get_list_by_key(dictionary: dict, key: str) -> list:
    """
    Получает список из словаря по ключу.
    """
    try:
        return dictionary[key]
    except KeyError:
        return []


def main():
    database = download_database_from_file()  # Загружаем базу данных из json файла

    while True:
        match menu.get_menu_item():
            case 0:  # Выход
                break
            case 1:  # Сформировать новую базу данных
                database = fill_database()
            case 2:  # Печать базы данных
                menu.print_database(database)
            case 3:  # Печать автомобилей
                cars = get_list_by_key(database, CARS)  # Получаем список автомобилей
                menu.print_cars(cars)
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
        save_database_to_file(database)  # Сохраняем базу данных в json файл


if __name__ == '__main__':
    main()

