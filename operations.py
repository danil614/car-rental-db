# Скрипт для выполнения операций с базой данных.

import create_elements  # Скрипт для заполнения базы данных
import input_data  # Скрипт для ввода данных
from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
import menu  # Скрипт для вывода сообщений
import datetime


def get_last_id(cars: list) -> int:
    """
    Возвращает последний id номер в списке автомобилей.
    """
    try:
        max_item = max(cars, key=lambda item: item[CAR.ID])  # Получаем элемент с максимальным id
        id_number = max_item[CAR.ID]  # Получаем максимальный id
    except ValueError:  # Пустой список
        id_number = -1
    except TypeError:  # В списке нет словаря
        id_number = -1
    except KeyError:  # Нет ключа в списке
        id_number = -1

    return id_number


def get_car_id(cars: list, index: int):
    """
    Возвращает id номер по индексу в списке автомобилей.
    """
    try:
        car = cars[index]
        car_id = car[CAR.ID]
    except IndexError:  # Выход за границы списка
        car_id = 0
    except KeyError:  # Не найден ключ id
        car_id = 0
    return car_id


def add_car(cars: list) -> dict:
    """
    Добавляет новый автомобиль в список автомобилей.
    """
    car = create_elements.create_car(
        id_number=get_last_id(cars) + 1,  # Получаем последний номер id, и берем следующий
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
    # Просим пользователя выбрать автомобиль для добавления истории
    car_index = menu.get_car_index(cars)

    # Получаем и проверяем дату аренды
    start_date_rent, end_date_rent = input_data.get_and_check_date_rent()

    story = create_elements.create_story(
        id_number=get_car_id(cars, car_index),  # Получаем id по индексу списка
        start_date_rent=start_date_rent,
        end_date_rent=end_date_rent
    )
    stories.append(story)  # Добавляем в список историй
    return story


if __name__ == '__main__':
    pass
    # print(add_car([{'id': 111}]))
    # print(add_driver([]))
    # print(add_story(create_elements.get_random_cars(10), []))
