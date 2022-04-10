# Скрипт для вывода сообщений пользователю.

import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
import get_elements  # Скрипт для получения элементов из базы данных


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_menu_item() -> int:
    """
    Выводит меню и получает выбранный пункт.
    """
    menu_text = '\n~~~~~~~~~~~~~~~~~~~ МЕНЮ ~~~~~~~~~~~~~~~~~~~\n' \
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
                '15. Отменить последнее изменение\n' \
                '0.  Выход\n' \
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

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
    print('|' + separator[1:-1] + '|')


def get_spaces(number: int):
    spaces = ''
    for _ in range(number):
        spaces += ' '
    return spaces
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////// Печать автомобилей /////////////////////////////////////////////////
def get_cars_title():
    cars_title = f'{CAR.LICENSE_PLATE:^16}|' \
                 f'{CAR.BRAND:^13}|' \
                 f'{CAR.MODEL:^13}|' \
                 f'{CAR.MAINTENANCE_DATE:^14}|'
    return cars_title


def print_cars_title():
    """
    Печатает заголовок таблицы автомобилей.
    """
    title = f'|{"N":^4}|' + get_cars_title()
    print()
    print(title)
    print_separator(title)


def get_car_string(car: dict):
    try:
        car_string = f'{car[CAR.LICENSE_PLATE]:^16}|' \
                     f' {car[CAR.BRAND]:<12}|' \
                     f' {car[CAR.MODEL]:<12}|' \
                     f'{car[CAR.MAINTENANCE_DATE]:^14}|'
    except KeyError:  # Ключ не найден
        car_string = get_spaces(59) + '|'
    return car_string


def print_car(index: int, car: dict):
    """
    Печатает строку таблицы автомобилей.
    """
    car_string = f'|{index + 1:^4}|' + get_car_string(car)
    print(car_string)  # Печатаем строку таблицы с данными автомобиля


def print_cars(cars: list):
    """
    Печатает таблицу автомобилей.
    """
    if not is_list_empty(cars, CARS):  # Если список не пустой
        print_cars_title()  # Печатаем заголовок таблицы
    for index, car in enumerate(cars):
        print_car(index, car)  # Выводим строку таблицы
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Печать водителей //////////////////////////////////////////////////
def print_drivers_title():
    """
    Печатает заголовок таблицы водителей.
    """
    title = f'|{"N":^4}|' \
            f'{DRIVER.NAME:^25}|' \
            f'{"Количество историй":^21}|'
    print()
    print(title)
    print_separator(title)


def print_driver(index: int, driver: dict):
    """
    Печатает строку таблицы водителей.
    """
    driver_string = f'|{index + 1:^4}|' \
                    f' {driver[DRIVER.NAME]:<24}|' \
                    f' {len(driver[DRIVER.STORIES]):<20}|'  # Количество историй
    print(driver_string)  # Печатаем строку таблицы с данными водителя


def print_drivers(drivers: list):
    """
    Печатает таблицу водителей.
    """
    if not is_list_empty(drivers, DRIVERS):  # Если список не пустой
        print_drivers_title()  # Печатаем заголовок таблицы
    for index, driver in enumerate(drivers):
        print_driver(index, driver)  # Выводим строку таблицы
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////// Печать историй по водителю /////////////////////////////////////////////
def print_stories_with_cars_title():
    """
    Печатает заголовок таблицы историй.
    """
    title = f'|{"N":^4}|' + \
            get_cars_title() + \
            f'{STORY.START_DATE_RENT:^26}|' \
            f'{STORY.END_DATE_RENT:^26}|'
    print()
    print(title)
    print_separator(title)


def print_story_with_car(index: int, story: dict, car: dict):
    """
    Печатает строку таблицы историй.
    """
    story_string = f'|{index + 1:^4}|' + \
                   get_car_string(car) + \
                   f'{story[STORY.START_DATE_RENT]:^26}|' \
                   f'{story[STORY.END_DATE_RENT]:^26}|'

    print(story_string)  # Печатаем строку таблицы с данными истории


def print_stories_with_cars(stories: list, cars: list):
    """
    Печатает строки для таблицы историй.
    """
    print_stories_with_cars_title()  # Печатаем заголовок таблицы историй
    for index, story in enumerate(stories):
        car = get_elements.get_car_by_id(cars, story[STORY.ID])
        print_story_with_car(index, story, car)  # Выводим строку таблицы


def print_stories_by_driver(cars: list, index_driver: int, driver: dict):
    """
    Печатает истории по водителю.
    """
    stories = driver[DRIVER.STORIES]  # Получаем истории водителя

    print_drivers_title()  # Печатаем заголовок таблицы
    print_driver(index_driver, driver)  # Выводим строку с данными водителя

    if len(stories) == 0:
        print('\nНет историй по данному водителю!')
    else:
        print_stories_with_cars(stories, cars)  # Выводим истории по водителю


def print_stories_by_drivers(cars: list, drivers: list):
    """
    Печатает таблицу водителей с историями.
    """
    is_list_empty(drivers, DRIVERS)
    for index, driver in enumerate(drivers):
        print_stories_by_driver(cars, index, driver)
        print('\n****************************************************************************************')
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////// Печать историй по автомобилю ////////////////////////////////////////////
def print_stories_with_drivers_title():
    """
    Печатает заголовок таблицы историй.
    """
    title = f'|{"N":^4}|' + \
            f'{DRIVER.NAME:^25}|' \
            f'{STORY.START_DATE_RENT:^26}|' \
            f'{STORY.END_DATE_RENT:^26}|'
    print()
    print(title)
    print_separator(title)


def print_story_with_driver(index: int, story: dict, driver: dict):
    """
    Печатает строку таблицы историй.
    """
    story_string = f'|{index + 1:^4}|' + \
                   f' {driver[DRIVER.NAME]:<24}|' \
                   f'{story[STORY.START_DATE_RENT]:^26}|' \
                   f'{story[STORY.END_DATE_RENT]:^26}|'

    print(story_string)  # Печатаем строку таблицы с данными истории


def print_stories_with_drivers(stories: list):
    """
    Печатает строки для таблицы историй.
    """
    print_stories_with_drivers_title()  # Печатаем заголовок таблицы историй
    for index, item in enumerate(stories):
        print_story_with_driver(index, item['story'], item['driver'])  # Выводим строку таблицы


def print_stories_by_car(drivers: list, index_car: int, car: dict):
    """
    Печатает истории по автомобилю.
    """
    stories = get_elements.get_stories_by_car(drivers, car)  # Получаем истории по автомобилю

    print_cars_title()  # Печатаем заголовок таблицы
    print_car(index_car, car)  # Выводим строку с данными автомобиля

    if len(stories) == 0:
        print('\nНет историй по данному автомобилю!')
    else:
        print_stories_with_drivers(stories)  # Выводим истории по автомобилю


def print_stories_by_cars(cars: list, drivers: list):
    """
    Печатает таблицу автомобилей с историями.
    """
    is_list_empty(cars, CARS)
    for index, car in enumerate(cars):
        print_stories_by_car(drivers, index, car)
        print('\n****************************************************************************************')
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
