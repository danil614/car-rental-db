# Скрипт для выполнения операций с базой данных.

import create_elements  # Скрипт для заполнения базы данных
import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
import menu  # Скрипт для вывода сообщений
import datetime
import get_elements  # Скрипт для получения элементов из базы данных


# ////////////////////////////////////////////// Добавление в базу данных //////////////////////////////////////////////
def add_car(cars: list) -> dict:
    """
    Добавляет новый автомобиль в список автомобилей.
    """
    car = create_elements.create_car(
        id_number=get_elements.get_last_id(cars) + 1,  # Получаем последний номер id, и берем следующий
        license_plate=input('Введите номерной знак: '),
        brand=input('Введите марку: '),
        model=input('Введите модель: '),
        maintenance_date=input_data.get_date('Введите дату ТО')
    )
    cars.append(car)  # Добавляем в список автомобилей
    return car


def add_driver(drivers: list) -> dict:
    """
    Добавляет нового водителя в список водителей.
    """
    driver = create_elements.create_driver(
        name=input('Введите ФИО водителя: '),
        stories=[]
    )
    drivers.append(driver)  # Добавляем в список водителей
    return driver


def add_story(cars: list, stories: list) -> dict:
    """
    Добавляет новую историю в список историй водителя.
    """
    # Просим пользователя выбрать автомобиль для добавления истории -----------------------------
    car = get_elements.get_selected_car(cars)

    # Получаем и проверяем даты аренды
    start_date_rent, end_date_rent = input_data.get_and_check_date_rent()

    story = create_elements.create_story(
        id_number=car[CAR.ID],  # Получаем id автомобиля --------------------------------------------------
        start_date_rent=start_date_rent,
        end_date_rent=end_date_rent
    )
    stories.append(story)  # Добавляем в список историй
    return story
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Изменение данных //////////////////////////////////////////////////
def edit_car(cars: list) -> dict:
    """
    Изменяет автомобиль в списке автомобилей. ---------------------------------- проверка на пустоту
    """
    car = get_elements.get_selected_car(cars)  # Просим пользователя выбрать автомобиль
    car[CAR.LICENSE_PLATE] = input('Введите номерной знак: '),
    car[CAR.BRAND] = input('Введите марку: '),
    car[CAR.MODEL] = input('Введите модель: '),
    car[CAR.MAINTENANCE_DATE] = input_data.get_date('Введите дату ТО')
    return car


def edit_driver(drivers: list) -> dict:
    """
    Изменяет водителя в списке водителей. ---------------------------------- проверка на пустоту
    """
    driver = get_elements.get_selected_driver(drivers)  # Просим пользователя выбрать водителя
    driver[DRIVER.NAME] = input('Введите ФИО водителя: ')
    return driver


def edit_story(cars: list, drivers: list):
    """
    Изменяет историю в списке историй по выбранному водителю. ---------------------------------- проверка на пустоту
    """
    driver = get_elements.get_selected_driver(drivers)  # Просим пользователя выбрать водителя
    stories = driver[DRIVER.STORIES]  # Получаем истории водителя

    if not menu.is_list_empty(stories, DRIVER.STORIES):
        # Просим пользователя выбрать историю
        story = get_elements.get_selected_story(stories)

        # Получаем и проверяем даты аренды
        start_date_rent, end_date_rent = input_data.get_and_check_date_rent()
        story[STORY.START_DATE_RENT] = start_date_rent
        story[STORY.END_DATE_RENT] = end_date_rent
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Удаление данных //////////////////////////////////////////////////
def delete_car(cars: list, drivers: list):
    car = get_elements.get_selected_car(cars)  # Просим пользователя выбрать автомобиль
    delete_stories_by_car(drivers, car)  # Удаляем истории, в которых используется id выбранного автомобиля
    cars.remove(car)  # Удаляем автомобиль из списка


def delete_stories_by_car(drivers: list, car: dict):
    id_car = car[CAR.ID]  # Получаем id автомобиля

    for driver in drivers:
        stories_by_driver = driver[DRIVER.STORIES]  # Получаем истории по водителю

        for story in stories_by_driver.copy():  # Идем по копии списка для удаления
            if story[STORY.ID] == id_car:
                # Если id совпал, удаляем историю
                stories_by_driver.remove(story)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


if __name__ == '__main__':
    pass
    # print(add_car([{'id': 111}]))
    # print(add_driver([]))
    # print(add_story(create_elements.get_random_cars(10), []))
