import json
JSON_FILE_NAME = 'database.json'


def save_json_file(data: dict):
    """
    Сохраняет данные в json файл.
    """
    try:  # Пробуем открыть файл
        json_file = open(JSON_FILE_NAME, 'w', encoding='UTF-8')
    except IOError:
        return False
    else:  # Если получилось, записываем в json
        with json_file:
            json.dump(data, json_file, ensure_ascii=False)
        return True


def get_data_from_json() -> dict:
    """
    Получает данные из json файла.
    """
    try:  # Пробуем открыть файл
        json_file = open(JSON_FILE_NAME, 'r', encoding='UTF-8')
    except IOError:
        data = {}
    else:  # Если получилось, считываем из json'а
        with json_file:
            data = json.load(json_file)

    return data


if __name__ == '__main__':
    pass
    # print(get_data_from_json())
    # print(save_json_file({'УРА!': 'ghbrjk@'}))
