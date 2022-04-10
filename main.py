# Вариант 10. Аренда автомобилей.

import operations
from create_elements import fill_database  # Скрипт для заполнения базы данных случайными значениями
import json_files  # Скрипт для работы с json файлами
import menu  # Скрипт для вывода сообщений
from keys import CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
import check_structure  # Скрипт для проверки структуры базы данных


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


def main():
    database = download_database_from_file()  # Загружаем базу данных из json файла
    cars, drivers = check_structure.main(database)  # Проверяем и исправляем структуру базы данных

    while True:
        match menu.get_menu_item():
            case 0:  # Выход
                break
            case 1:  # Сформировать новую базу данных
                database = fill_database()
                cars = check_structure.get_list_by_key(database, CARS)  # Получаем список автомобилей
                drivers = check_structure.get_list_by_key(database, DRIVERS)  # Получаем список водителей
            case 2:  # Печать автомобилей
                if not menu.is_list_empty(cars, CARS):
                    menu.print_cars(cars)
            case 3:  # Печать водителей
                if not menu.is_list_empty(drivers, DRIVERS):
                    menu.print_drivers(drivers)
            case 4:  # Печать историй по автомобилю
                menu.print_stories_by_cars(cars, drivers)
            case 5:  # Печать историй по водителю
                menu.print_stories_by_drivers(drivers)
            case 6:  # Добавить автомобиль
                operations.add_car(cars)
            case 7:  # Добавить водителя
                operations.add_driver(drivers)
            case 8:  # Добавить историю
                operations.add_story(cars, drivers)
            case 9:  # Изменить автомобиль
                operations.edit_car(cars)
            case 10:  # Изменить водителя
                operations.edit_driver(drivers)
            case 11:  # Изменить историю
                operations.edit_story(drivers)
            case 12:  # Удалить автомобиль
                operations.delete_car(cars, drivers)
            case 13:  # Удалить водителя
                operations.delete_driver(drivers)
            case 14:  # Удалить историю
                operations.delete_story(drivers)
            case _:
                print('Неправильно введен номер пункта меню!')
        save_database_to_file(database)  # Сохраняем базу данных в json файл
        input('Нажмите Enter для продолжения...')


if __name__ == '__main__':
    main()
