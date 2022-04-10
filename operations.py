# Скрипт для выполнения операций с базой данных.

import create_elements  # Скрипт для заполнения базы данных
import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY  # Скрипт, в котором хранятся строковые ключи
import menu  # Скрипт для вывода сообщений
import get_elements  # Скрипт для получения элементов из базы данных


# ////////////////////////////////////////////// Добавление в базу данных //////////////////////////////////////////////
def add_car(cars: list) -> (list, dict):
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
    return cars, car


def add_driver(drivers: list) -> (list, dict):
    """
    Добавляет нового водителя в список водителей.
    """
    driver = create_elements.create_driver(
        name=input('Введите ФИО водителя: '),
        stories=[]
    )
    drivers.append(driver)  # Добавляем в список водителей
    menu.print_drivers(drivers)  # Выводим всех водителей
    return drivers, driver


def add_story(cars: list, drivers: list) -> (list, dict):
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

        if car is not None:  # Если список автомобилей не пустой
            # Получаем и проверяем даты аренды
            start_date_rent, end_date_rent = input_data.get_and_check_date_rent()
            story = create_elements.create_story(
                id_number=car[CAR.ID],  # Получаем id автомобиля
                start_date_rent=start_date_rent,
                end_date_rent=end_date_rent
            )

            stories = driver[DRIVER.STORIES]  # Получаем истории водителя
            stories.append(story)  # Добавляем в список историй
            index_driver = drivers.index(driver)  # Получаем индекс водителя
            menu.print_stories_by_driver(cars, index_driver, driver)  # Выводим список историй
            return stories, story

    return None, None  # Если не получилось добавить

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Изменение данных //////////////////////////////////////////////////
def edit_car(cars: list) -> (list, dict, dict):
    """
    Изменяет автомобиль в списке автомобилей.
    """
    # Просим пользователя выбрать автомобиль
    car = get_elements.get_selected_car(
        cars=cars,
        message='Введите номер автомобиля для редактирования'
    )
    old_car = car.copy()  # Делаем копию автомобиля

    if car is not None:  # Если список автомобилей не пустой
        # Редактируем данные автомобиля
        car[CAR.LICENSE_PLATE] = input('Введите номерной знак: ')
        car[CAR.BRAND] = input('Введите марку: ')
        car[CAR.MODEL] = input('Введите модель: ')
        car[CAR.MAINTENANCE_DATE] = input_data.get_date('Введите дату ТО').isoformat()  # Преобразуем дату в строку
        menu.print_cars(cars)  # Выводим автомобили
        return cars, car, old_car

    return None, None, None  # Если не получилось добавить


def edit_driver(drivers: list) -> (list, dict, dict):
    """
    Изменяет водителя в списке водителей.
    """
    # Просим пользователя выбрать водителя
    driver = get_elements.get_selected_driver(
        drivers=drivers,
        message='Введите номер водителя для редактирования'
    )
    old_driver = driver.copy()

    if driver is not None:  # Если список водителей не пустой
        driver[DRIVER.NAME] = input('Введите ФИО водителя: ')  # Редактируем ФИО водителя
        menu.print_drivers(drivers)  # Выводим всех водителей
        return drivers, driver, old_driver

    return None, None, None  # Если не получилось добавить


def edit_story(cars: list, drivers: list) -> (list, dict, dict):
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
            cars=cars,
            message='Введите номер истории для редактирования'
        )
        old_story = story.copy()

        if story is not None:  # Если список историй не пустой
            # Получаем и проверяем даты аренды
            start_date_rent, end_date_rent = input_data.get_and_check_date_rent()
            story[STORY.START_DATE_RENT] = start_date_rent.isoformat()  # Преобразуем дату в строку
            story[STORY.END_DATE_RENT] = end_date_rent.isoformat()  # Преобразуем дату в строку

            index_driver = drivers.index(driver)  # Получаем индекс водителя
            menu.print_stories_by_driver(cars, index_driver, driver)  # Выводим список историй
            return stories, story, old_story

    return None, None, None  # Если не получилось добавить
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////// Удаление данных //////////////////////////////////////////////////
def delete_car(cars: list, drivers: list) -> (list, dict, list):
    """
    Удаляет водителя из списка водителей, а также связанные с ним истории.
    """
    # Просим пользователя выбрать автомобиль
    car = get_elements.get_selected_car(
        cars=cars,
        message='Введите номер автомобиля для удаления'
    )

    if car is not None:  # Если список автомобилей не пустой
        old_stories = get_elements.get_stories_by_car(drivers, car)  # Получаем истории, которые будут удалены

        # Удаляем истории, в которых используется id выбранного автомобиля
        get_elements.delete_stories_by_car(drivers, car)
        cars.remove(car)  # Удаляем автомобиль из списка
        menu.print_stories_by_cars(cars, drivers)  # Выводим все автомобили с их историями
        return cars, car, old_stories

    return None, None, None  # Если не получилось добавить


def delete_driver(drivers: list) -> (list, dict):
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
        return drivers, driver

    return None, None  # Если не получилось добавить


def delete_story(cars: list, drivers: list) -> (list, dict):
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
            cars=cars,
            message='Введите номер истории для удаления'
        )

        if story is not None:  # Если список историй не пустой
            stories.remove(story)  # Удаляем выбранную историю

            index_driver = drivers.index(driver)  # Получаем индекс водителя
            menu.print_stories_by_driver(cars, index_driver, driver)  # Выводим список историй
            return stories, story

    return None, None  # Если не получилось добавить
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
