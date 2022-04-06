# Скрипт для заполнения базы данных.

import datetime
from random import randint
from pprint import pprint
import values  # Скрипт для получения случайных значений полей базы данных


# Количество автомобилей
MIN_CARS_NUMBER = 5
MAX_CARS_NUMBER = 10


# Количество водителей
MIN_DRIVERS_NUMBER = 5
MAX_DRIVERS_NUMBER = 10

# Количество историй аренды у водителя
MIN_STORIES_NUMBER = 1
MAX_STORIES_NUMBER = 5


# ----------------------------------------------
def get_last_id():
    id_number = 0
    return id_number
# ----------------------------------------------


def create_car(id_number: int, license_plate: str, brand: str, model: str, maintenance_date: datetime) -> dict:
    """
    Создает словарь-автомобиль по входным данным.
    """
    car = {
        'id': id_number,
        'Гос. номер': license_plate,
        'Марка': brand,
        'Модель': model,
        'Дата ТО': maintenance_date
    }

    return car


def create_driver(name: str, stories: list) -> dict:
    """
    Создает словарь-водителя по входным данным.
    """
    driver = {
        'ФИО': name,
        'История': stories
    }

    return driver


def create_story(id_number: int, start_date_rent: datetime, end_date_rent: datetime) -> dict:
    """
    Создает словарь-историю аренды по входным данным.
    """
    story = {
        'id': id_number,
        'Дата начала аренды': start_date_rent,
        'Дата окончания аренды': end_date_rent
    }

    return story


def get_random_cars(cars_number: int) -> list:
    """
    Возвращает список автомобилей.
    """
    cars = []

    for i in range(cars_number):
        brand, model = values.get_brand_and_model()

        car = create_car(id_number=i, license_plate=values.get_license_plate(),
                         brand=brand, model=model, maintenance_date=values.get_random_date())
        cars.append(car)

    return cars


def get_random_stories(stories_number: int, last_id_number: int) -> list:
    stories = []

    for i in range(stories_number):
        id_number = randint(0, last_id_number)  # Присваиваем случайный id
        end_date_rent = values.get_random_date()

        # Вычитаем случайное количество дней из даты конца аренды
        start_date_rent = end_date_rent - values.get_random_days(7, 180)

        story = create_story(id_number=id_number, start_date_rent=start_date_rent, end_date_rent=end_date_rent)
        stories.append(story)

    return stories


def get_random_drivers(drivers_number: int, cars_number: int) -> list:
    """
    Возвращает список водителей.
    """
    drivers = []

    for i in range(drivers_number):
        # Генерируем случайное количество историй водителя
        stories_number = randint(MIN_STORIES_NUMBER, MAX_STORIES_NUMBER)
        stories = get_random_stories(stories_number=stories_number, last_id_number=cars_number - 1)

        driver = create_driver(name=values.get_name(), stories=stories)
        drivers.append(driver)

    return drivers


def fill_database() -> dict:
    """
    Заполняет базу данных случайными значениями.
    """
    cars_number = randint(MIN_CARS_NUMBER, MAX_CARS_NUMBER)
    cars = get_random_cars(cars_number)

    drivers_number = randint(MIN_DRIVERS_NUMBER, MAX_DRIVERS_NUMBER)
    drivers = get_random_drivers(drivers_number, cars_number)

    car_rental = {'Автомобили': cars, 'Водители': drivers}
    return car_rental


if __name__ == '__main__':
    pass
    # database = fill_database()
    # pprint(database)
