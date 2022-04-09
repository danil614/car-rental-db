# Скрипт для вывода сообщений пользователю.

from pprint import pprint
import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи


def get_menu_item() -> int:
    """
    Выводит меню и получает выбранный пункт.
    """
    menu_text = '\n~~~~~~~~~~~~~~~~~~~~~~~~~~ МЕНЮ ~~~~~~~~~~~~~~~~~~~~~~~~~~\n' \
                '1.  Сформировать новую базу данных\n' \
                '2.  Печать автомобилей\n' \
                '3.  Печать водителей\n' \
                '4.  Печать историй по автомобилю\n' \
                '5.  Печать историй по водителю\n' \
                '6.  Добавить автомобиль\n' \
                '7.  Добавить водителя\n' \
                '8.  Добавить историю\n' \
                '9.  Изменить автомобиль\n' \
                '10. Изменить водителя\n'\
                '11. Изменить историю\n' \
                '12. Удалить автомобиль\n' \
                '13. Удалить водителя\n'\
                '14. Удалить историю\n' \
                '0.  Выход\n'

    print(menu_text)
    return input_data.get_int_number('Выберите пункт меню', 0)


def is_list_empty(check_list: list, name_list: str) -> bool:
    """
    Проверяет список на пустоту.
    """
    try:  # Пробуем получить длину списка
        length = len(check_list)
    except TypeError:  # Ошибка, если был передан не list
        length = 0

    if length == 0:  # Если пустой, выдаем ошибку
        print(f'Список "{name_list}" пустой!')
        return True
    else:
        return False


def print_separator(title: str):
    """
    Печатает разделитель заголовка таблицы.
    """
    separator = ''
    for _ in title:
        # По количеству символов заголовка будем составлять разделитель
        separator += '-'
    print(separator)


# ///////////////////////////////////////////////// Печать автомобилей /////////////////////////////////////////////////
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
    if is_list_empty(cars, CARS):  # Проверяем на пустоту
        return

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
    index_car = input_data.get_int_number('\nВведите номер автомобиля', 1, len(cars)) - 1
    return index_car
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Печать водителей //////////////////////////////////////////////////
def print_drivers_title() -> int:
    """
    Печатает заголовок таблицы автомобилей.
    """
    title = f'{"N":^4}|' \
            f'{DRIVER.NAME:^25}|' \
            f'{"Количество историй":^21}|'

    print(title)
    print_separator(title)
    return len(title)


def print_drivers(drivers: list):
    """
    Печатает строки для таблицы автомобилей.
    """
    if is_list_empty(drivers, DRIVERS):  # Проверяем на пустоту
        return

    print()
    length_title = print_drivers_title()  # Печатаем заголовок таблицы

    for number, driver in enumerate(drivers):
        try:  # Пробуем получить данные автомобиля
            driver_string = f'{number + 1:^4}|' \
                            f' {driver[DRIVER.NAME]:<24}|' \
                            f' {len(driver[DRIVER.STORIES]):<20}|'  # Количество историй
        except (KeyError, TypeError):  # Отлавливаем ошибку, если ключа нет или нет длины историй
            driver_string = 'ошибка чтения строки из базы данных'
            driver_string = f'{number + 1:^4}|' \
                            f'{driver_string:^{length_title - 5}}'
        print(driver_string)  # Печатаем строку таблицы с данными автомобиля


def get_driver_index(drivers: list) -> int:
    """
    Выводит список автомобилей и возвращает выбранный автомобиль.
    """
    print_drivers(drivers)
    index_driver = input_data.get_int_number('\nВведите номер водителя', 1, len(drivers)) - 1
    return index_driver
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
