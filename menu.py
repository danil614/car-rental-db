# Скрипт для вывода сообщений пользователю.

import get_elements
import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY  # Скрипт, в котором хранятся строковые ключи


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////// Печать автомобилей /////////////////////////////////////////////////
def print_cars_title():
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


def print_car(index: int, car: dict):
    """
    Печатает строку таблицы автомобилей.
    """
    car_string = f'{index + 1:^4}|' \
                 f'{car[CAR.LICENSE_PLATE]:^16}|' \
                 f' {car[CAR.BRAND]:<12}|' \
                 f' {car[CAR.MODEL]:<12}|' \
                 f'{car[CAR.MAINTENANCE_DATE]:^14}'
    print(car_string)  # Печатаем строку таблицы с данными автомобиля


def print_cars(cars: list):
    """
    Печатает таблицу автомобилей.
    """
    print_cars_title()  # Печатаем заголовок таблицы
    for index, car in enumerate(cars):
        print_car(index, car)  # Выводим строку таблицы
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Печать водителей //////////////////////////////////////////////////
def print_drivers_title():
    """
    Печатает заголовок таблицы водителей.
    """
    title = f'{"N":^4}|' \
            f'{DRIVER.NAME:^25}|' \
            f'{"Количество историй":^21}|'
    print()
    print(title)
    print_separator(title)


def print_driver(index: int, driver: dict):
    """
    Печатает строку таблицы водителей.
    """
    driver_string = f'{index + 1:^4}|' \
                    f' {driver[DRIVER.NAME]:<24}|' \
                    f' {len(driver[DRIVER.STORIES]):<20}|'  # Количество историй
    print(driver_string)  # Печатаем строку таблицы с данными водителя


def print_drivers(drivers: list):
    """
    Печатает таблицу водителей.
    """
    print_drivers_title()  # Печатаем заголовок таблицы
    for index, driver in enumerate(drivers):
        print_driver(index, driver)  # Выводим строку таблицы
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////// Печать историй ///////////////////////////////////////////////////
def print_stories_title():
    """
    Печатает заголовок таблицы историй.
    """
    title = f'{"N":^4}|' \
            f'{STORY.START_DATE_RENT:^26}|' \
            f'{STORY.END_DATE_RENT:^26}'
    print()
    print(title)
    print_separator(title)


def print_story(index: int, story: dict):
    """
    Печатает строку таблицы историй.
    """
    story_string = f'{index + 1:^4}|' \
                   f'{story[STORY.START_DATE_RENT]:^26}|' \
                   f'{story[STORY.END_DATE_RENT]:^26}'
    print(story_string)  # Печатаем строку таблицы с данными истории


def print_stories(stories: list):
    """
    Печатает строки для таблицы историй.
    """
    print_stories_title()  # Печатаем заголовок таблицы историй
    for index, story in enumerate(stories):
        print_story(index, story)  # Выводим строку таблицы


def print_stories_by_cars(cars: list, drivers: list):
    """
    Печатает таблицу автомобилей с историями.
    """
    print_cars_title()  # Печатаем заголовок таблицы
    for index, car in enumerate(cars):
        print_car(index, car)  # Выводим строку с данными автомобиля

        # Выводим истории по автомобилю
        print_stories(
            stories=get_elements.get_stories_by_car(drivers, car)
        )


def print_stories_by_drivers(drivers: list):
    """
    Печатает таблицу водителей с историями.
    """
    print_drivers_title()  # Печатаем заголовок таблицы
    for index, driver in enumerate(drivers):
        print_driver(index, driver)  # Выводим строку с данными водителя

        # Выводим истории по водителю
        print_stories(
            stories=driver[DRIVER.STORIES]
        )
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
