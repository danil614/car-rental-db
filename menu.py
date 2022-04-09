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
    print()
    print(title)
    print_separator(title)
    return len(title)


def print_car(index: int, car: dict, length_title: int):
    """
    Печатает строку таблицы автомобилей.
    """
    try:  # Пробуем получить данные автомобиля
        car_string = f'{index + 1:^4}|' \
                     f'{car[CAR.LICENSE_PLATE]:^16}|' \
                     f' {car[CAR.BRAND]:<12}|' \
                     f' {car[CAR.MODEL]:<12}|' \
                     f'{car[CAR.MAINTENANCE_DATE]:^14}'
    except (KeyError, TypeError):  # Отлавливаем ошибку, если ключа нет или элемент не словарь
        car_string = 'ошибка чтения строки из базы данных'
        car_string = f'{index + 1:^4}|' \
                     f'{car_string:^{length_title - 5}}'
    print(car_string)  # Печатаем строку таблицы с данными автомобиля


def print_cars(cars: list):
    """
    Печатает строки для таблицы автомобилей.
    """
    length_title = print_cars_title()  # Печатаем заголовок таблицы
    for index, car in enumerate(cars):
        print_car(index, car, length_title)  # Выводим строку таблицы


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
    Печатает заголовок таблицы водителей.
    """
    title = f'{"N":^4}|' \
            f'{DRIVER.NAME:^25}|' \
            f'{"Количество историй":^21}|'
    print()
    print(title)
    print_separator(title)
    return len(title)


def print_driver(index: int, driver: dict, length_title: int):
    """
    Печатает строку таблицы водителей.
    """
    try:  # Пробуем получить данные водителя
        driver_string = f'{index + 1:^4}|' \
                        f' {driver[DRIVER.NAME]:<24}|' \
                        f' {len(driver[DRIVER.STORIES]):<20}|'  # Количество историй
    except (KeyError, TypeError):  # Отлавливаем ошибку, если ключа нет или нет длины историй
        driver_string = 'ошибка чтения строки из базы данных'
        driver_string = f'{index + 1:^4}|' \
                        f'{driver_string:^{length_title - 5}}'
    print(driver_string)  # Печатаем строку таблицы с данными водителя


def print_drivers(drivers: list):
    """
    Печатает строки для таблицы водителей.
    """
    length_title = print_drivers_title()  # Печатаем заголовок таблицы
    for index, driver in enumerate(drivers):
        print_driver(index, driver, length_title)  # Выводим строку таблицы


def get_driver_index(drivers: list) -> int:
    """
    Выводит список водителей и выбранного водителя.
    """
    print_drivers(drivers)
    index_driver = input_data.get_int_number('\nВведите номер водителя', 1, len(drivers)) - 1
    return index_driver
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////// Печать историй ///////////////////////////////////////////////////
def print_stories_title() -> int:
    """
    Печатает заголовок таблицы историй.
    """
    title = f'{"N":^4}|' \
            f'{STORY.START_DATE_RENT:^26}|' \
            f'{STORY.END_DATE_RENT:^26}'
    print()
    print(title)
    print_separator(title)
    return len(title)


def print_story(index: int, story: dict, length_title: int):
    """
    Печатает строку таблицы историй.
    """
    try:  # Пробуем получить данные истории
        story_string = f'{index + 1:^4}|' \
                       f'{story[STORY.START_DATE_RENT]:^26}|' \
                       f'{story[STORY.END_DATE_RENT]:^26}'
    except KeyError:  # Отлавливаем ошибку, если ключа нет
        story_string = 'ошибка чтения строки из базы данных'
        story_string = f'{index + 1:^4}|' \
                       f'{story_string:^{length_title - 5}}'
    print(story_string)  # Печатаем строку таблицы с данными истории


def print_stories(stories: list):
    """
    Печатает строки для таблицы историй.
    """
    if is_list_empty(stories, DRIVER.STORIES):  # Проверяем на пустоту
        return

    length_title = print_stories_title()  # Печатаем заголовок таблицы историй
    for index, story in enumerate(stories):
        print_story(index, story, length_title)


def print_stories_by_car(index: int, car: dict, stories: list):
    """
    Печатает строки для таблицы историй по автомобилю.
    """
    length_cars_title = print_cars_title()
    print_car(index, car, length_cars_title)
    print_stories(stories)


def print_stories_by_driver(index: int, driver: dict, stories: list):
    """
    Печатает строки для таблицы историй по водителю.
    """
    length_drivers_title = print_drivers_title()
    print_driver(index, driver, length_drivers_title)
    print_stories(stories)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
