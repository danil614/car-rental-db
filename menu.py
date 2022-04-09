# Скрипт для вывода сообщений пользователю.

from pprint import pprint
import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи


def get_menu_item() -> int:
    """
    Выводит меню и получает выбранный пункт.
    """
    menu_text = '\n~~~~~~~~~~~~~~~~~~~~~~~~~~ МЕНЮ ~~~~~~~~~~~~~~~~~~~~~~~~~~\n' \
                '1. Сформировать новую базу данных\n' \
                '2. Печать базы данных\n' \
                '3. Печать автомобилей\n' \
                '4. \n' \
                '5. \n' \
                '6. \n' \
                '7. \n' \
                '8. \n' \
                '0. Выход\n'

    print(menu_text)
    return input_data.get_int_number('Выберите пункт меню', 0)


def print_database(database: dict):
    """
    Печатает базу данных.
    """
    pprint(database)


def print_separator(title: str):
    """
    Печатает разделитель заголовка таблицы.
    """
    separator = ''
    for _ in title:
        # По количеству символов заголовка будем составлять разделитель
        separator += '-'
    print(separator)


def print_cars_title() -> int:
    """
    Печатает заголовок таблицы автомобилей.
    """
    title = f'{"N":^4}|' \
            f'{CAR.LICENSE_PLATE:^16}|' \
            f'{CAR.BRAND:^13}|' \
            f'{CAR.MODEL:^13}|' \
            f'{CAR.MAINTENANCE_DATE:^14}'
    print(title)
    print_separator(title)
    return len(title)


def print_cars(cars: list):
    """
    Печатает строки для таблицы автомобилей.
    """
    print()
    length_title = print_cars_title()  # Печатаем заголовок таблицы
    for number, car in enumerate(cars):
        try:  # Пробуем получить данные автомобиля
            car_string = f'{number + 1:^4}|' \
                         f'{car[CAR.LICENSE_PLATE]:^16}|' \
                         f' {car[CAR.BRAND]:<12}|' \
                         f' {car[CAR.MODEL]:<12}|' \
                         f'{car[CAR.MAINTENANCE_DATE]:^14}'
        except KeyError:  # Отлавливаем ошибку, если ключа нет
            car_string = 'ошибка чтения строки из базы данных'
            car_string = f'{number + 1:^4}|' \
                         f'{car_string:^{length_title - 5}}'
        print(car_string)  # Печатаем строку таблицы с данными автомобиля


def get_car_index(cars: list) -> int:
    """
    Выводит список автомобилей и возвращает выбранный автомобиль.
    """
    print_cars(cars)
    index_car = input_data.get_int_number('\nВыберите номер автомобиля', 1, len(cars)) - 1
    return index_car
