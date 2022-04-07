# Скрипт для получения случайных значений полей базы данных.

from random import randint, choice
from datetime import date, timedelta  # Библиотека для работы с датой

MALE_NAMES = ['Андрей', 'Алексей', 'Афанасий', 'Александр', 'Аркадий', 'Анатолий', 'Арсений', 'Антон', 'Богдан',
              'Борис', 'Виктор', 'Вадим', 'Валерий', 'Василий', 'Владимир', 'Георгий', 'Глеб', 'Елисей', 'Егор',
              'Евгений', 'Захар', 'Игорь', 'Илья', 'Иосиф', 'Лев', 'Макар', 'Матвей', 'Николай', 'Никита', 'Олег',
              'Павел', 'Петр', 'Роман', 'Сергей', 'Феликс', 'Федор', 'Юрий', 'Ярослав', 'Яков']

FEMALE_NAMES = ['Агния', 'Алена', 'Александра', 'Алина', 'Алиса', 'Алла', 'Анна', 'Анастасия', 'Ангелина', 'Арина',
                'Белла', 'Валентина', 'Варвара', 'Вера', 'Вероника', 'Владлена', 'Ева', 'Евгения', 'Екатерина',
                'Елена', 'Елизавета', 'Жанна', 'Зоя', 'Ирина', 'Карина', 'Каролина', 'Кира', 'Лариса', 'Лилия',
                'Маргарита', 'Мария', 'Надежда', 'Наталья', 'Оксана', 'Полина', 'Регина', 'Сабина', 'Юлия', 'Яна']

SURNAMES = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков',
            'Федоров', 'Морозов', 'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров', 'Павлов', 'Козлов',
            'Степанов', 'Николаев', 'Орлов', 'Андреев', 'Макаров', 'Никитин', 'Захаров', 'Зайцев', 'Соловьев',
            'Борисов', 'Яковлев', 'Григорьев', 'Романов', 'Воробьев', 'Сергеев', 'Кузьмин', 'Фролов', 'Александров',
            'Дмитриев', 'Королев', 'Гусев', 'Киселев', 'Ильин', 'Поляков', 'Сорокин']

# Буквы автомобильного номера
LICENSE_PLATE_LETTERS = 'АВЕКМНОРСТУХ'

CAR_NAMES = [
    'Skoda Octavia', 'Mitsubishi Lancer', 'Toyota Corolla', 'Honda Civic', 'Porsche 911', 'BMW 3',
    'Volkswagen Golf', 'Москвич 412', 'Opel Corsa', 'Tesla Model 3', 'Volvo 200', 'Ferrari 360', 'Lada Granta',
    'Lada Vesta', 'Toyota Camry', 'УАЗ Патриот', 'Lada Largus', 'Hyundai Solaris', 'Haval F7', 'Lada Priora',
    'Hyundai Creta', 'Mitsubishi Outlander', 'Kia Rio', 'Volkswagen Polo', 'Ford Focus', 'Mazda CX-5'
]


# Количество дней для генерации даты
MIN_DAYS_NUMBER = 30
MAX_DAYS_NUMBER = 2000


def get_name() -> str:
    """
    Возвращает имя и фамилию человека.
    """
    name = choice(SURNAMES)

    if randint(0, 1) == 0:
        name += ' ' + choice(MALE_NAMES)
    else:
        # Для женских имен будем добавлять букву "а" к фамилии
        name += 'а ' + choice(FEMALE_NAMES)

    return name


def get_license_plate() -> str:
    """
    Возвращает номерной знак автомобиля.
    """
    license_plate = f'{choice(LICENSE_PLATE_LETTERS)} ' \
                    f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)} ' \
                    f'{choice(LICENSE_PLATE_LETTERS)}{choice(LICENSE_PLATE_LETTERS)} ' \
                    f'{randint(0, 9)}{randint(0, 9)}'
    return license_plate


def get_brand_and_model():
    """
    Возвращает марку и модель автомобиля.
    """
    car_name = choice(CAR_NAMES).split()

    try:
        brand = car_name[0]
        model = car_name[1]
    except IndexError:
        brand = 'NoBrand'
        model = 'NoModel'

    return brand, model


def get_random_days(min_days_number: int, max_days_number: int):
    """
    Возвращает случайное количество дней в формате даты.
    """
    return timedelta(days=randint(min_days_number, max_days_number))


def get_random_date():
    """
    Возвращает случайную дату.
    """
    current_date = date.today()
    random_days = get_random_days(MIN_DAYS_NUMBER, MAX_DAYS_NUMBER)
    # Вычитаем из текущей даты случайное количество дней
    return current_date - random_days


if __name__ == '__main__':
    pass
    # print(get_random_date())
    # print(get_brand_and_model())
    # print(get_license_plate())
    # print(get_name())
