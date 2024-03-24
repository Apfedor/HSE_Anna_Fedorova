"""
1. Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле traders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла traders.txt в файл traders.csv.
"""

import json

keys = ('inn', 'ogrn', 'address')

def Example_dz5_1():


    with open( "traders.txt", 'r') as f:
        inn_list: list = [l[:10] for l in f.readlines()]

    with open( 'traders.json') as f:
        traders: tuple = json.load(f)

    traders_list = [search_for_traders(traders, inn) for inn in inn_list]

    delimiter = '; '  # разделитель таблицы
    export_csv: str = delimiter.join(keys) + '\n'
    for trader_data in traders_list:
        export_csv += delimiter.join([trader_data[key] for key in keys]) + '\n'

    with open( 'traders.csv', 'w', newline='') as f:
        f.write(export_csv)

    with open( 'traders.csv', 'r') as f:
        print(f.read())

    pass


def search_for_traders(traders: tuple, inn: str) -> dict:
    for trader in traders:
        if trader['inn'] == inn:
            my_trader: dict = {key: trader[key] for key in keys}
            break
    return my_trader


Example_dz5_1()
