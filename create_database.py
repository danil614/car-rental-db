import datetime


def create_car(id_number: int, license_plate: str, brand: str, model: str, maintenance_date: datetime):
    car = {
        'id': id_number,
        'Гос. номер': license_plate,
        'Марка': brand,
        'Модель': model,
        'Дата ТО': maintenance_date
    }

    return car


def create_driver(name: str, stories: list):
    driver = {
        'ФИО': name,
        'История': stories
    }

    return driver


def create_story(id_number: int, start_date_rent: datetime, end_date_rent: datetime):
    story = {
        'id': id_number,
        'Дата начала аренды': start_date_rent,
        'Дата окончания аренды': end_date_rent
    }

    return story
