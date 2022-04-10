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
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////// Работа с историями /////////////////////////////////////////////////
def stories_by_car(drivers: list, car: dict, operation):
    """
    Перебирает все истории и выполняет действие при совпадении id.

    :param drivers: Список водителей

    :param car: Автомобиль

    :param operation: Действие с историей
    """
    id_car = car[CAR.ID]  # Получаем id автомобиля

    for driver in drivers:
        stories_by_driver = driver[DRIVER.STORIES]  # Получаем истории по водителю

        for story in stories_by_driver.copy():  # Идем по копии списка для удаления
            if story[STORY.ID] == id_car:
                operation(stories_by_driver, story)  # При совпадении id, выполняем функцию


def get_stories_by_car(drivers: list, car: dict) -> list:
    """
    Возвращает истории по автомобилю.
    """
    stories = []
    stories_by_car(drivers=drivers,
                   car=car,
                   operation=lambda _, story: stories.append(story)  # Добавляем в список историй
                   )
    return stories


def delete_stories_by_car(drivers: list, car: dict):
    """
    Удаляет истории по автомобилю.
    """
    stories_by_car(drivers=drivers,
                   car=car,
                   operation=lambda stories_by_driver, story: stories_by_driver.remove(story)  # Удаляем историю
                   )
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////// Выбор элементов из списка //////////////////////////////////////////////
def get_selected_dictionary_in_list(input_list: list, name_list: str, message: str, print_function) -> (dict, None):
    """
    Выводит список и возвращает выбранный словарь.

    :param input_list: Список для печати и выбора из него

    :param name_list: Название списка

    :param message: Сообщения для выбора из списка

    :param print_function: Функция печати

    :return: Выбранный словарь
    """
    if menu.is_list_empty(input_list, name_list):  # Проверяем список на пустоту
        return None
    else:
        # Выводим список
        print_function(input_list)
        # Просим пользователя выбрать элемент
        index = input_data.get_int_number('\n' + message, 1, len(input_list)) - 1
        # Получаем словарь по индексу
        dictionary = input_list[index]
        return dictionary


def get_selected_car(cars: list, message: str) -> (dict, None):
    """
    Выводит список автомобилей и возвращает выбранный автомобиль.
    """
    car = get_selected_dictionary_in_list(
        input_list=cars,
        name_list=CARS,
        message=message,
        print_function=menu.print_cars
    )
    return car


def get_selected_driver(drivers: list, message: str) -> (dict, None):
    """
    Выводит список водителей и возвращает выбранного водителя.
    """
    driver = get_selected_dictionary_in_list(
        input_list=drivers,
        name_list=DRIVERS,
        message=message,
        print_function=menu.print_drivers
    )
    return driver


def get_selected_story(stories: list, message: str) -> (dict, None):
    """
    Выводит список историй и возвращает выбранную историю.
    """
    story = get_selected_dictionary_in_list(
        input_list=stories,
        name_list=DRIVER.STORIES,
        message=message,
        print_function=menu.print_stories
    )
    return story
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
