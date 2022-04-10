# Вариант 10. Аренда автомобилей.

import operations  # Скрипт для выполнения операций с базой данных
from create_elements import fill_database  # Скрипт для заполнения базы данных случайными значениями
import json_files  # Скрипт для работы с json файлами
import menu  # Скрипт для вывода сообщений
from keys import CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
import check_structure  # Скрипт для проверки структуры базы данных
import get_elements  # Скрипт для получения элементов из базы данных
from undo_changes import catch_change, undo_change  # Скрипт для отмены внесенных изменений в базу данных


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def print_stories_by_car(cars: list, drivers: list):
    # Просим пользователя выбрать автомобиль
    car = get_elements.get_selected_car(
        cars=cars,
        message='Введите номер автомобиля для печати истории'
    )
    if car is not None:  # Если список автомобилей не пустой
        index = cars.index(car)
        menu.print_stories_by_car(drivers, index, car)


def print_stories_by_driver(cars: list, drivers: list):
    # Просим пользователя выбрать водителя
    driver = get_elements.get_selected_driver(
        drivers=drivers,
        message='Введите номер водителя для добавления истории'
    )
    if driver is not None:  # Если список водителей не пустой
        index = drivers.index(driver)
        menu.print_stories_by_driver(cars, index, driver)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def main():
    database = download_database_from_file()  # Загружаем базу данных из json файла
    cars, drivers = check_structure.main(database)  # Проверяем и исправляем структуру базы данных
    changes = []  # Список внесенных изменений

    while True:
        menu_item = menu.get_menu_item()  # Просим пользователя выбрать пункт меню
        changed_list, changed_item, old_item, old_stories = None, None, None, None  # Параметры изменения данных
        match menu_item:
            case 0:  # Выход
                break
            case 1:  # Сформировать новую базу данных
                database = fill_database()
                print('\nНовая база данных сформирована!')
                cars = check_structure.get_list_by_key(database, CARS)  # Получаем список автомобилей
                drivers = check_structure.get_list_by_key(database, DRIVERS)  # Получаем список водителей
            case 2:  # Печать автомобилей
                if not menu.is_list_empty(cars, CARS):
                    menu.print_cars(cars)
            case 3:  # Печать водителей
                if not menu.is_list_empty(drivers, DRIVERS):
                    menu.print_drivers(drivers)
            case 4:  # Печать историй по автомобилю
                print_stories_by_car(cars, drivers)
            case 5:  # Печать историй по водителю
                print_stories_by_driver(cars, drivers)
            case 6:  # Добавить автомобиль
                changed_list, changed_item = operations.add_car(cars)
            case 7:  # Добавить водителя
                changed_list, changed_item = operations.add_driver(drivers)
            case 8:  # Добавить историю
                changed_list, changed_item = operations.add_story(cars, drivers)
            case 9:  # Изменить автомобиль
                changed_list, changed_item, old_item = operations.edit_car(cars)
            case 10:  # Изменить водителя
                changed_list, changed_item, old_item = operations.edit_driver(drivers)
            case 11:  # Изменить историю
                changed_list, changed_item, old_item = operations.edit_story(cars, drivers)
            case 12:  # Удалить автомобиль
                changed_list, changed_item, old_stories = operations.delete_car(cars, drivers)
            case 13:  # Удалить водителя
                changed_list, changed_item = operations.delete_driver(drivers)
            case 14:  # Удалить историю
                changed_list, changed_item = operations.delete_story(cars, drivers)
            case 15:  # Отменить последнее изменение
                undo_change(changes)
            case _:
                print('Неправильно введен номер пункта меню!')
        save_database_to_file(database)  # Сохраняем базу данных в json файл
        catch_change(menu_item, changed_list, changed_item, old_item, old_stories, changes)  # Ловим изменение
        _ = input('\nНажмите Enter для продолжения... ')


if __name__ == '__main__':
    main()
