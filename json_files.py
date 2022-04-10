# Скрипт для работы с json файлами.

import json
JSON_FILE_NAME = 'database.json'


def save_json_file(data: dict) -> bool:
    """
    Сохраняет данные в json файл.
    """
    try:  # Пробуем открыть файл и записать json
        json_file = open(JSON_FILE_NAME, 'w', encoding='UTF-8')
        with json_file:
            json.dump(data, json_file, ensure_ascii=False)
        return True
    except IOError:  # Ошибка записи файла
        return False
    except TypeError:  # Ошибка кодирования файла в json
        return False


def get_data_from_json() -> dict:
    """
    Получает данные из json файла.
    """
    try:  # Пробуем открыть файл и считать json
        json_file = open(JSON_FILE_NAME, 'r', encoding='UTF-8')
        with json_file:
            data = json.load(json_file)

        if isinstance(data, dict):  # Проверяем data на тип dict
            return data
        else:
            return {}
    except IOError:  # Ошибка открытия файла
        return {}
    except json.decoder.JSONDecodeError:  # Ошибка при декодировании json
        return {}
