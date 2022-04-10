# Скрипт для получения элементов из базы данных.

from keys import CAR, DRIVER, STORY, CARS, DRIVERS  # Скрипт, в котором хранятся строковые ключи
import menu  # Скрипт для вывода сообщений
import input_data


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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


# def get_car_id_by_index(cars: list, index: int) -> int:
#     """
#     Возвращает id номер по индексу в списке автомобилей.
#     """
#     try:
#         car = cars[index]
#         id_car = car[CAR.ID]
#     except KeyError:  # Не найден ключ id
#         id_car = -1
#     except IndexError:  # Выход за границы списка
#         id_car = -1
#
#     return id_car
#
#
# def get_value_in_dictionary_by_key(dictionary: dict, key: str):
#     try:
#         return dictionary[key]
#     except KeyError:  # Не найден ключ id
#         return None
#
#
# def get_value_in_list_by_index(input_list: list, index: int):
#     try:
#         return input_list[index]
#     except IndexError:  # Выход за границы списка
#         return None
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_selected_car(cars: list) -> dict:
    """
    Выводит список автомобилей и возвращает выбранный автомобиль.
    """
    menu.print_cars(cars)  # Выводим список автомобилей
    # Просим пользователя выбрать автомобиль
    index = input_data.get_int_number('\nВведите номер автомобиля', 1, len(cars)) - 1
    car = cars[index]  # Получаем автомобиль по индексу
    return car


def get_selected_driver(drivers: list) -> dict:
    """
    Выводит список водителей и возвращает выбранного водителя.
    """
    menu.print_drivers(drivers)  # Выводим список водителей
    # Просим пользователя выбрать водителя
    index = input_data.get_int_number('\nВведите номер водителя', 1, len(drivers)) - 1
    driver = drivers[index]  # Получаем водителя по индексу
    return driver


def get_selected_story(stories: list) -> dict:
    menu.print_stories(stories)
    # Просим пользователя выбрать историю
    index = input_data.get_int_number('\nВведите номер истории', 1, len(stories)) - 1
    story = stories[index]  # Получаем историю по индексу
    return story
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def get_stories_by_driver(drivers: list, driver: dict):
#     """
#     Получает список историй по водителю.
#     """
#     driver = drivers[index]  # Получаем водителя
#     stories = driver[DRIVER.STORIES]  # Получаем истории водителя
#     return stories


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



# def get_car_id(cars: list, index: int) -> int:
#     """
#     Возвращает id номер по индексу в списке автомобилей.
#     """
#     try:
#         car = cars[index]
#         id_car = car[CAR.ID]
#     except KeyError:  # Не найден ключ id
#         id_car = -1
#     except IndexError:  # Выход за границы списка
#         id_car = -1
#
#     return id_car



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def get_dictionary_by_index(input_list: list, index: int) -> dict:  # Проверка на list???
#     """
#     Получает словарь из списка по индексу.
#     """
#     try:
#         dictionary = input_list[index]
#     except IndexError:  # Выход за границы списка или тип не dict
#         input_list.append({})  # Добавляем пустой словарь в конец списка
#         dictionary = input_list[-1]  # Получаем последний элемент
#     else:
#         if not isinstance(dictionary, dict):  # Если тип не dict
#             input_list[index] = {}  # Добавляем пустой словарь по индексу
#             dictionary = input_list[index]  # Получаем элемент по индексу
#     return dictionary
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
