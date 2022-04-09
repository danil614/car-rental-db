# Вариант 10. Аренда автомобилей.
import create_elements
import operations
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
        input_list = dictionary[key]  # Получаем список по ключу
        if not isinstance(input_list, list):  # Проверяем на тип list
            raise ValueError
    except (KeyError, ValueError):
        # При ошибках перезаписываем пустой список
        input_list = rewrite_list_by_key(dictionary, key)

    return input_list


def rewrite_list_by_key(dictionary: dict, key: str) -> list:
    """
    Перезаписывает список в словарь по ключу.
    Если в базе данных были ошибки, то происходит перезапись.
    """
    dictionary[key] = []  # Записываем пустой список по ключу
    return dictionary[key]


def get_stories(drivers: list):
    """
    Получает список историй по водителю.
    """
    # Просим пользователя выбрать водителя
    index_driver = menu.get_driver_index(drivers)
    try:
        driver = drivers[index_driver]
    except IndexError:
        driver = {}
    return get_list_by_key(driver, DRIVER.STORIES)


def main():
    database = download_database_from_file()  # Загружаем базу данных из json файла
    cars = get_list_by_key(database, CARS)  # Получаем список автомобилей
    drivers = get_list_by_key(database, DRIVERS)  # Получаем список водителей

    while True:
        match menu.get_menu_item():
            case 0:  # Выход
                break
            case 1:  # Сформировать новую базу данных
                database = fill_database()
                cars = get_list_by_key(database, CARS)  # Получаем список автомобилей
                drivers = get_list_by_key(database, DRIVERS)  # Получаем список водителей
            case 2:  # Печать автомобилей
                menu.print_cars(cars)
            case 3:  # Печать водителей
                menu.print_drivers(drivers)
            case 4:  #
                pass
            case 5:  #
                pass
            case 6:  # Добавить автомобиль
                operations.add_car(cars)
                menu.print_cars(cars)
            case 7:  # Добавить водителя
                operations.add_driver(drivers)
                menu.print_drivers(drivers)
            case 8:  # Добавить историю
                if not (menu.is_list_empty(cars, CARS) or menu.is_list_empty(drivers, DRIVERS)):  # ---------
                    stories = get_stories(drivers)  # Получаем истории по водителю
                    operations.add_story(cars, stories)
                    # Печать историй по водителю ------------------------------------------------------------
            case _:
                print('Неправильно введен номер пункта меню!')
        save_database_to_file(database)  # Сохраняем базу данных в json файл
        input('Нажмите Enter для продолжения...')


if __name__ == '__main__':
    main()
