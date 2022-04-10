# Скрипт для отмены внесенных изменений в базу данных.

from keys import DRIVER  # Скрипт, в котором хранятся строковые ключи


class OPERATIONS:
    ADD = 'add'
    EDIT = 'edit'
    DELETE = 'delete'


def add_deleted_stories(stories: list):
    """
    Добавляет удаленные истории.
    """
    if stories is None:
        # Если истории None, не будем их перебирать
        return

    for item in stories:
        driver: dict = item['driver']  # Получаем водителя
        story: dict = item['story']  # Получаем историю
        stories_by_driver: list = driver[DRIVER.STORIES]  # Получаем истории водителя
        stories_by_driver.append(story)


def undo_change(changes: list):
    """
    Отменяет последнее изменение.
    :param changes: Список всех изменений.
    """
    if len(changes) == 0:
        print('\nНет действий для отмены!')
        return

    last_change: dict = changes[-1]  # Получаем последнее изменение
    operation: str = last_change['operation']
    changed_list: list = last_change['changed_list']
    changed_item: dict = last_change['changed_item']
    old_item: dict = last_change['old_item']
    old_stories: list = last_change['old_stories']

    match operation:
        case OPERATIONS.ADD:  # При добавлении
            changed_list.remove(changed_item)  # Удаляем добавленный элемент
        case OPERATIONS.EDIT:
            index_item = changed_list.index(changed_item)  # Получаем индекс элемента
            changed_list[index_item] = old_item  # Присваиваем старые данные
        case OPERATIONS.DELETE:
            changed_list.append(changed_item)  # Добавляем удаленный элемент
            # Добавляем удаленные истории, которые были удалены при удалении автомобиля
            add_deleted_stories(old_stories)

    changes.pop(-1)  # Удаляем отмененное действие
    print('\nПоследнее действие было отменено!')


def catch_change(menu_item: int,
                 changed_list: list,
                 changed_item: dict,
                 old_item: dict,
                 old_stories: list,
                 changes: list):
    """
    Сохраняет изменения в список изменений.

    :param menu_item: Выбранный пункт меню.
    :param changed_list: Измененный список.
    :param changed_item: Измененный элемент.
    :param old_item: Элемент до изменения.
    :param old_stories: Список элемнтов до изменения.
    :param changes: Список всех изменений.
    """
    operation = get_operation(menu_item)  # Получаем текстовую операцию

    if operation is None:
        return

    if changed_list is None or changed_item is None:
        # Если какой-то из списков None, то не будем добавлять изменения
        return

    match operation:
        case OPERATIONS.ADD:
            pass
        case OPERATIONS.EDIT:
            if old_item is None:
                # Если старый элемент None, то не будем добавлять изменения
                return
        case OPERATIONS.DELETE:
            pass
        case _:
            return

    # Когда все параметры известны, добавляем в изменения
    changes.append(
        dict(operation=operation,
             changed_list=changed_list,
             changed_item=changed_item,
             old_item=old_item,
             old_stories=old_stories
             )
    )


def get_operation(menu_item: int):
    """
    Возвращает текстовую операцию по пункту меню.

    :param menu_item: Выбранный пункт меню.
    :return: Текстовая операция.
    """
    match menu_item:
        case 1:  # Сформировать новую базу данных
            return None
        case 6:  # Добавить автомобиль
            return OPERATIONS.ADD
        case 7:  # Добавить водителя
            return OPERATIONS.ADD
        case 8:  # Добавить историю
            return OPERATIONS.ADD
        case 9:  # Изменить автомобиль
            return OPERATIONS.EDIT
        case 10:  # Изменить водителя
            return OPERATIONS.EDIT
        case 11:  # Изменить историю
            return OPERATIONS.EDIT
        case 12:  # Удалить автомобиль
            return OPERATIONS.DELETE
        case 13:  # Удалить водителя
            return OPERATIONS.DELETE
        case 14:  # Удалить историю
            return OPERATIONS.DELETE
        case _:
            return None
