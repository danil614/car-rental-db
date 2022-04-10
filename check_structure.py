# Скрипт для проверки структуры базы данных

from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи


# ////////////////////////////////////////// Проверка данных на корректность ///////////////////////////////////////////
def is_id_number_correct(id_number: int) -> bool:
    """
    Проверяет на корректность id номер.
    """
    if isinstance(id_number, int):  # Проверяем id номер на тип int
        return True
    else:
        return False


def is_car_correct(car: dict) -> bool:
    """
    Проверяет на корректность данные автомобиля.
    """
    if isinstance(car, dict):  # Проверяем автомобиль на тип dict
        try:  # Пробуем получить данные автомобиля
            id_number = car[CAR.ID]
            _ = car[CAR.LICENSE_PLATE]
            _ = car[CAR.BRAND]
            _ = car[CAR.MODEL]
            _ = car[CAR.MAINTENANCE_DATE]
        except KeyError:  # Отлавливаем ошибку, если какого-то ключа нет
            return False
        else:
            return is_id_number_correct(id_number)  # Проверяем на корректность id автомобиля
    else:
        return False


def is_driver_correct(driver: dict):
    """
    Проверяет на корректность данные водителя.
    """
    if isinstance(driver, dict):  # Проверяем водителя на тип dict
        try:  # Пробуем получить данные водителя
            _ = driver[DRIVER.NAME]
        except KeyError:  # Отлавливаем ошибку, если какого-то ключа нет
            return False
        else:
            # Получаем список историй по водителю
            # Если истории повреждены, будем перезаписывать пустой список
            stories = get_list_by_key(driver, DRIVER.STORIES)

            # Удаляем некорректные истории у водителя
            delete_incorrect_data(stories, is_story_correct)
            return True


def is_story_correct(story: dict) -> bool:
    """
    Проверяет на корректность данные истории.
    """
    if isinstance(story, dict):  # Проверяем историю на тип dict
        try:  # Пробуем получить данные истории
            id_number = story[STORY.ID]
            _ = story[STORY.START_DATE_RENT]
            _ = story[STORY.END_DATE_RENT]
        except KeyError:  # Отлавливаем ошибку, если какого-то ключа нет
            return False
        else:
            return is_id_number_correct(id_number)  # Проверяем на корректность id истории
    else:
        return False
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_list_by_key(dictionary: dict, key: str) -> list:
    """
    Получает список из словаря по ключу.
    Если в базе данных были ошибки, то происходит перезапись значения.
    """
    try:
        input_list = dictionary[key]  # Получаем список по ключу
    except KeyError:  # Нет ключа в словаре
        input_list = rewrite_list_by_key(dictionary, key, [])  # Перезаписываем в значение пустой список
    else:
        if not isinstance(input_list, list):  # Если тип не list
            input_list = rewrite_list_by_key(dictionary, key, [])  # Перезаписываем в значение пустой список

    return input_list


def rewrite_list_by_key(dictionary: dict, key: str, new_list: list) -> list:
    """
    Перезаписывает список в словарь по ключу.
    """
    dictionary[key] = new_list  # Записываем новый список по ключу
    return dictionary[key]


def delete_incorrect_data(input_list: list, is_correct):
    """
    Удаляет из списка некорректные элементы.
    """
    [input_list.remove(item) for item in input_list.copy() if not is_correct(item)]
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main(database: dict):
    """
    Проверяет структуры базы данных.
    """
    cars = get_list_by_key(database, CARS)  # Получаем список автомобилей
    delete_incorrect_data(cars, is_car_correct)  # Удаляем некорректные автомобили в списке автомобилей

    drivers = get_list_by_key(database, DRIVERS)  # Получаем список водителей
    delete_incorrect_data(drivers, is_driver_correct)  # Удаляем некорректных водителей в списке водителей

    return cars, drivers
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
