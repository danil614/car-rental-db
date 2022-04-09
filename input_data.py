# Скрипт для проверки входных данных.

import datetime
import sys


def get_int_number(message: str, left_border: int, right_border: int = sys.maxsize) -> int:
    """
    Проверяет введенное число int на правильность ввода и выход за границы.
    """
    number = 0
    correct = False

    while not correct:
        try:  # проверяем корректно ли введено число int
            number = int(input(message + ': '))
            if right_border >= number >= left_border:  # проверяем выходит ли число за пределы значений
                correct = True
            else:
                print('Число выходит за пределы допустимых значений! Введите его еще раз')
        except ValueError:
            print('Неправильно введено число! Введите его еще раз')

    return number


def get_date(message: str) -> datetime:
    """
    Проверяет введенную дату на правильность ввода и выход за границы.
    """
    date = datetime.date.min
    correct = False
    print('------ ' + message + ' ------')

    while not correct:
        try:
            year = get_int_number('Введите год', 1)
            month = get_int_number('Введите месяц', 1)
            day = get_int_number('Введите день', 1)

            date = datetime.date(year, month, day)  # Преобразуем в формат даты
            correct = True
        except ValueError:
            print('Неправильно введена дата! Введите ее еще раз')

    return date


def get_and_check_date_rent():
    """
    Запрашивает даты, и проверяет, что дата начала меньше даты конца.
    """
    start_date_rent = datetime.date.min  # Дата начала аренды
    end_date_rent = datetime.date.min  # Дата конца аренды
    correct = False

    while not correct:
        start_date_rent = get_date('\nВведите дату начала аренды')
        end_date_rent = get_date('Введите дату окончания аренды')

        if start_date_rent > end_date_rent:  # Проверка дат
            correct = False
            print('\nДата начала больше чем дата конца! Введите даты еще раз')
        else:
            correct = True

    return start_date_rent, end_date_rent
