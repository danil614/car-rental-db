# Вариант 10. Аренда автомобилей.
import create_elements
import operations
from create_elements import fill_database  # Скрипт для заполнения базы данных случайными значениями
import input_data  # Скрипт для ввода данных
import json_files  # Скрипт для работы с json файлами
import menu  # Скрипт для вывода сообщений
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
from pprint import pprint
import get_elements  # Скрипт для получения элементов из базы данных
import check_structure

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
    # cars = get_elements.get_list_by_key(database, CARS)  # Получаем список автомобилей
    # drivers = get_elements.get_list_by_key(database, DRIVERS)  # Получаем список водителей
    cars, drivers = check_structure.main(database)

    while True:
        match menu.get_menu_item():
            case 0:  # Выход
                break
            case 1:  # Сформировать новую базу данных
                database = fill_database()
                cars = check_structure.get_list_by_key(database, CARS)  # Получаем список автомобилей
                drivers = check_structure.get_list_by_key(database, DRIVERS)  # Получаем список водителей
            case 2:  # Печать автомобилей
                menu.print_cars(cars)
            case 3:  # Печать водителей
                menu.print_drivers(drivers)
            case 4:  # Печать историй по автомобилю
                if not menu.is_list_empty(cars, CARS):
                    index = menu.get_car_index(cars)  # Спрашиваем у пользователя индекс автомобиля
                    car = cars[index]  # Получаем автомобиль по индексу

                    id_car = get_elements.get_car_id(cars, index)  # Получаем id автомобиля по индексу
                    stories = get_elements.get_stories_by_car_id(drivers, id_car)  # Получаем истории по автомобилю

                    menu.print_stories_by_car(index, car, stories)  # Выводим все истории автомобиля
            case 5:  # Печать историй по водителю
                if not menu.is_list_empty(drivers, DRIVERS):
                    index = menu.get_driver_index(drivers)  # Спрашиваем у пользователя индекс водителя
                    driver = drivers[index]  # Получаем водителя по индексу
                    stories = get_elements.get_stories_by_driver_index(drivers, index)  # Получаем истории по водителю
                    menu.print_stories_by_driver(index, driver, stories)  # Выводим все истории водителя
            case 6:  # Добавить автомобиль
                operations.add_car(cars)
                menu.print_cars(cars)
            case 7:  # Добавить водителя
                operations.add_driver(drivers)
                menu.print_drivers(drivers)
            case 8:  # Добавить историю
                if not (menu.is_list_empty(cars, CARS) or menu.is_list_empty(drivers, DRIVERS)):  # ---------
                    index = menu.get_driver_index(drivers)  # Просим пользователя выбрать водителя
                    stories = get_elements.get_stories_by_driver_index(drivers, index)  # Получаем истории по водителю
                    operations.add_story(cars, stories)
                    # Печать историй по водителю ------------------------------------------------------------
            case _:
                print('Неправильно введен номер пункта меню!')
        save_database_to_file(database)  # Сохраняем базу данных в json файл
        input('Нажмите Enter для продолжения...')


if __name__ == '__main__':
    main()
