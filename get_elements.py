# Скрипт для получения элементов из базы данных.

from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
import menu  # Скрипт для вывода сообщений


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
    except KeyError:  # Нет ключа в словаре
        id_number = -1

    return id_number


def get_car_id(cars: list, index: int) -> int:
    """
    Возвращает id номер по индексу в списке автомобилей.
    """
    car = get_dictionary_by_index(cars, index)
    try:
        id_car = car[CAR.ID]
    except KeyError:  # Не найден ключ id
        id_car = -1

    return id_car


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_stories_by_driver_index(drivers: list, index: int):
    """
    Получает список историй по водителю.
    """
    driver = get_dictionary_by_index(drivers, index)  # Получаем водителя
    stories = driver[DRIVER.STORIES]  # Получаем истории водителя
    return stories


def get_stories_by_car_id(drivers: list, id_car: int) -> list:
    """
    Возвращает список историй по id автомобиля.
    """
    stories = []
    for index, _ in enumerate(drivers):
        stories_by_driver = get_stories_by_driver_index(drivers, index)  # Получаем истории у водителя по индексу

        for story in stories_by_driver:
            try:
                id_story = story[STORY.ID]
                if id_story == id_car:  # Если id совпадает, то добавляем в список всех историй
                    stories.append(story)
            except (KeyError, TypeError):  # Если нет ключа или тип не словарь, то пропускаем
                pass

    return stories
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_dictionary_by_index(input_list: list, index: int) -> dict:  # Проверка на list???
    """
    Получает словарь из списка по индексу.
    """
    try:
        dictionary = input_list[index]
    except IndexError:  # Выход за границы списка или тип не dict
        input_list.append({})  # Добавляем пустой словарь в конец списка
        dictionary = input_list[-1]  # Получаем последний элемент
    else:
        if not isinstance(dictionary, dict):  # Если тип не dict
            input_list[index] = {}  # Добавляем пустой словарь по индексу
            dictionary = input_list[index]  # Получаем элемент по индексу
    return dictionary
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
