import json
from pprint import pprint


def save_json_file(data):
    with open('test.json', 'w', encoding='UTF-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)


def add_owner(owners):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    owner_id = max(owners, key=lambda item: item['id'])['id'] + 1
    owner = dict(id=owner_id, name=name, age=age)
    owners.append(owner)
    print(owner)


def del_prop(property):
    print('Выберите, кого удалять')
    print_prop(property)
    numb = input()
    property.pop(numb)


def get_list_indexes(ownership, id_owner):
    return [index for index, item in enumerate(ownership) if item['id_own'] == id_owner]


def print_prop(prop):
    for numb, elem in enumerate(prop):
        print(numb + 1, ' - ',
              f'{elem["type"]}')


def del_owner(owners, ownership):
    print('Выберите, кого удалять')
    numb = int(input())
    id_owner = owners[numb - 1]['id']
    list_indexes = get_list_indexes(ownership, id_owner)
    for index in list_indexes[::-1]:
        ownership.pop(index)

    owners.pop(numb)


def main():
    with open('test.json', 'r', encoding='UTF-8') as json_file:
        data = json.load(json_file)

    owners = data['Владельцы']
    ownership = data['Недвижимость']

    pprint(owners)
    pprint(ownership)

    # add_owner(owners)
    del_owner(owners, ownership)

    save_json_file(data)


if __name__ == '__main__':
    main()
