# -*- coding: utf-8 -*-
import json
from sys import platform
import math

JSON_FILE = 'Бары.json'

def load_data(filepath) -> list:
    with open(filepath, mode='r', encoding="utf-8") as file:
        return json.load(file)


def get_biggest_bar(data) -> dict:
    return max(data, key=lambda el: el['Cells']['SeatsCount'])


def get_smallest_bar(data) -> dict:
    return min(data, key=lambda el: el['Cells']['SeatsCount'])


def get_closest_bar(data, longitude, latitude) -> dict:
    return min(data, key=lambda el: math.sqrt(
        (el['Cells']['geoData']['coordinates'][0] - longitude)**2 +
        (el['Cells']['geoData']['coordinates'][1] - latitude)**2))


if __name__ == '__main__':
    latitude = float(input('Введите широту вашего местоположения:'))
    longitude = float(input('Введите долготу вашего местоположения:'))

    data = load_data(JSON_FILE)

    if platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()

    print('Бар с мин. кол-вом мест:\n', get_smallest_bar(data), '\n')
    print('Бар с макс. кол-вом мест:\n', get_biggest_bar(data), '\n')
    print('Самый близкий бар:\n', get_closest_bar(data, longitude, latitude),
          '\n')
