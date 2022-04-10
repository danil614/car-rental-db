# Скрипт для выполнения операций с базой данных.

import create_elements  # Скрипт для заполнения базы данных
import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY  # Скрипт, в котором хранятся строковые ключи
import menu  # Скрипт для вывода сообщений
import get_elements  # Скрипт для получения элементов из базы данных


# ////////////////////////////////////////////// Добавление в базу данных //////////////////////////////////////////////
def add_car(cars: list):
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
    menu.print_cars(cars)  # Выводим автомобили


def add_driver(drivers: list):
    """
    Добавляет нового водителя в список водителей.
    """
    driver = create_elements.create_driver(
        name=input('Введите ФИО водителя: '),
        stories=[]
    )
    drivers.append(driver)  # Добавляем в список водителей
    menu.print_drivers(drivers)  # Выводим всех водителей


def add_story(cars: list, drivers: list):
    """
    Добавляет новую историю в список историй водителя.
    """
    # Просим пользователя выбрать водителя
    driver = get_elements.get_selected_driver(
        drivers=drivers,
        message='Введите номер водителя для добавления истории'
    )

    if driver is not None:  # Если список водителей не пустой
        # Просим пользователя выбрать автомобиль
        car = get_elements.get_selected_car(
            cars=cars,
            message='Введите номер автомобиля для добавления истории'
        )

        # Получаем и проверяем даты аренды
        start_date_rent, end_date_rent = input_data.get_and_check_date_rent()
        story = create_elements.create_story(
            id_number=car[CAR.ID],  # Получаем id автомобиля
            start_date_rent=start_date_rent,
            end_date_rent=end_date_rent
        )

        stories = driver[DRIVER.STORIES]  # Получаем истории водителя
        stories.append(story)  # Добавляем в список историй
        menu.print_stories(stories)  # Выводим список историй
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Изменение данных //////////////////////////////////////////////////
def edit_car(cars: list):
    """
    Изменяет автомобиль в списке автомобилей.
    """
    # Просим пользователя выбрать автомобиль
    car = get_elements.get_selected_car(
        cars=cars,
        message='Введите номер автомобиля для редактирования'
    )

    if car is not None:  # Если список автомобилей не пустой
        # Редактируем данные автомобиля
        car[CAR.LICENSE_PLATE] = input('Введите номерной знак: '),
        car[CAR.BRAND] = input('Введите марку: '),
        car[CAR.MODEL] = input('Введите модель: '),
        car[CAR.MAINTENANCE_DATE] = input_data.get_date('Введите дату ТО')
        menu.print_cars(cars)  # Выводим автомобили


def edit_driver(drivers: list):
    """
    Изменяет водителя в списке водителей.
    """
    # Просим пользователя выбрать водителя
    driver = get_elements.get_selected_driver(
        drivers=drivers,
        message='Введите номер водителя для редактирования'
    )

    if driver is not None:  # Если список водителей не пустой
        driver[DRIVER.NAME] = input('Введите ФИО водителя: ')  # Редактируем ФИО водителя
        menu.print_drivers(drivers)  # Выводим всех водителей


def edit_story(drivers: list):
    """
    Изменяет историю в списке историй по выбранному водителю.
    """
    # Просим пользователя выбрать водителя
    driver = get_elements.get_selected_driver(
        drivers=drivers,
        message='Введите номер водителя для выбора в нем истории'
    )

    if driver is not None:  # Если список водителей не пустой
        stories = driver[DRIVER.STORIES]  # Получаем истории водителя
        # Просим пользователя выбрать историю
        story = get_elements.get_selected_story(
            stories=stories,
            message='Введите номер истории для редактирования'
        )

        if story is not None:  # Если список историй не пустой
            # Получаем и проверяем даты аренды
            start_date_rent, end_date_rent = input_data.get_and_check_date_rent()
            story[STORY.START_DATE_RENT] = start_date_rent
            story[STORY.END_DATE_RENT] = end_date_rent
            menu.print_stories(stories)  # Выводим список историй
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Удаление данных //////////////////////////////////////////////////
def delete_car(cars: list, drivers: list):
    """
    Удаляет водителя из списка водителей, а также связанные с ним истории.
    """
    # Просим пользователя выбрать автомобиль
    car = get_elements.get_selected_car(
        cars=cars,
        message='Введите номер автомобиля для удаления'
    )

    if car is not None:  # Если список автомобилей не пустой
        # Удаляем истории, в которых используется id выбранного автомобиля
        get_elements.delete_stories_by_car(drivers, car)
        cars.remove(car)  # Удаляем автомобиль из списка
        menu.print_stories_by_cars(cars, drivers)  # Выводим все автомобили с их историями


def delete_driver(drivers: list):
    """
    Удаляет водителя из списка водителей.
    """
    # Просим пользователя выбрать водителя
    driver = get_elements.get_selected_driver(
        drivers=drivers,
        message='Введите номер водителя для удаления'
    )

    if driver is not None:  # Если список водителей не пустой
        drivers.remove(driver)  # Удаляем водителя из списка
        menu.print_drivers(drivers)  # Выводим всех водителей


def delete_story(drivers: list):
    """
    Удаляет историю по водителю.
    """
    # Просим пользователя выбрать водителя
    driver = get_elements.get_selected_driver(
        drivers=drivers,
        message='Введите номер водителя для выбора в нем истории'
    )

    if driver is not None:  # Если список водителей не пустой
        stories = driver[DRIVER.STORIES]  # Получаем истории водителя
        # Просим пользователя выбрать историю
        story = get_elements.get_selected_story(
            stories=stories,
            message='Введите номер истории для удаления'
        )

        if story is not None:  # Если список историй не пустой
            stories.remove(story)  # Удаляем выбранную историю
            menu.print_stories(stories)  # Выводим список историй
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
