# Скрипт для заполнения базы данных.

import datetime
from random import randint
import values  # Скрипт для получения случайных значений полей базы данных
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи

# Количество случайных автомобилей
MIN_CARS_NUMBER = 5
MAX_CARS_NUMBER = 10

# Количество случайных водителей
MIN_DRIVERS_NUMBER = 5
MAX_DRIVERS_NUMBER = 10

# Количество случайных историй аренды у водителя
MIN_STORIES_NUMBER = 1
MAX_STORIES_NUMBER = 5


# ///////////////////////////////////////////////// Создание словарей //////////////////////////////////////////////////
def create_car(id_number: int, license_plate: str, brand: str, model: str, maintenance_date: datetime) -> dict:
    """
    Создает словарь-автомобиль по входным данным.
    """
    car = {
        CAR.ID: id_number,
        CAR.LICENSE_PLATE: license_plate,
        CAR.BRAND: brand,
        CAR.MODEL: model,
        CAR.MAINTENANCE_DATE: maintenance_date.isoformat()  # Преобразуем дату в строку
    }

    return car


def create_driver(name: str, stories: list) -> dict:
    """
    Создает словарь-водителя по входным данным.
    """
    driver = {
        DRIVER.NAME: name,
        DRIVER.STORIES: stories
    }

    return driver


def create_story(id_number: int, start_date_rent: datetime, end_date_rent: datetime) -> dict:
    """
    Создает словарь-историю аренды по входным данным.
    """
    story = {
        STORY.ID: id_number,
        STORY.START_DATE_RENT: start_date_rent.isoformat(),  # Преобразуем дату в строку
        STORY.END_DATE_RENT: end_date_rent.isoformat()
    }

    return story
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////// Создание случайных списков /////////////////////////////////////////////
def get_random_cars(cars_number: int) -> list:
    """
    Возвращает список случайных автомобилей.
    """
    cars = []

    for i in range(cars_number):
        brand, model = values.get_brand_and_model()

        # Создаем автомобиль и заполняем его случайными значениями
        car = create_car(
            id_number=i,
            license_plate=values.get_license_plate(),
            brand=brand,
            model=model,
            maintenance_date=values.get_random_date()
        )
        cars.append(car)
    return cars


def get_random_stories(stories_number: int, last_id_number: int) -> list:
    """
    Возвращает список случайных историй.
    """
    stories = []

    for i in range(stories_number):
        id_number = randint(0, last_id_number)  # Присваиваем случайный id
        end_date_rent = values.get_random_date()  # Присваиваем случайную дату

        # Вычитаем случайное количество дней из даты конца аренды
        start_date_rent = end_date_rent - values.get_random_days(7, 180)

        story = create_story(id_number=id_number, start_date_rent=start_date_rent, end_date_rent=end_date_rent)
        stories.append(story)

    return stories


def get_random_drivers(drivers_number: int, cars_number: int) -> list:
    """
    Возвращает список случайных водителей.
    """
    drivers = []

    for i in range(drivers_number):
        # Генерируем случайное количество историй водителя
        stories_number = randint(MIN_STORIES_NUMBER, MAX_STORIES_NUMBER)
        stories = get_random_stories(
            stories_number=stories_number,
            last_id_number=cars_number - 1
        )

        # Записываем случайное ФИО и случайные истории
        driver = create_driver(name=values.get_name(), stories=stories)
        drivers.append(driver)

    return drivers
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def fill_database() -> dict:
    """
    Заполняет базу данных случайными значениями.
    """
    cars_number = randint(MIN_CARS_NUMBER, MAX_CARS_NUMBER)  # Получаем случайное количество автомобилей
    cars = get_random_cars(cars_number)

    drivers_number = randint(MIN_DRIVERS_NUMBER, MAX_DRIVERS_NUMBER)  # Получаем случайное количество водителей
    drivers = get_random_drivers(drivers_number, cars_number)

    car_rental = {CARS: cars, DRIVERS: drivers}
    return car_rental
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
