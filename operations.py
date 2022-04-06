# Скрипт для выполнения операций с базой данных.

import create_elements  # Скрипт для заполнения базы данных
import input_data  # Скрипт для ввода данных


def get_last_id(cars: list) -> int:
    """
    Возвращает последний id номер в списке автомобилей.
    """
    try:
        max_item = max(cars, key=lambda item: item['id'])
        id_number = max_item['id']
    except ValueError:  # Пустой список
        id_number = -1
    except TypeError:  # В списке нет словаря
        id_number = -1
    except KeyError:  # Нет ключа в списке
        id_number = -1

    return id_number


def add_car(cars: list) -> dict:
    car = create_elements.create_car(
        id_number=get_last_id(cars) + 1,  # Получаем последний номер id, и берем следующий
        license_plate=input('Введите номерной знак: '),
        brand=input('Введите марку: '),
        model=input('Введите модель: '),
        maintenance_date=input_data.get_date('Введите дату ТО'))
    return car


def add_driver():
    pass


if __name__ == '__main__':
    print(add_car([{'id': 0}]))
