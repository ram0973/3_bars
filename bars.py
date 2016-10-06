# -*- coding: utf-8 -*-
import argparse
import json
import os
from sys import platform
import math
import sys


def get_named_argument(arg_name: str) -> str:
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument('--' + arg_name)
        return getattr(parser.parse_args(sys.argv[1:]), arg_name)
    else:
        print('Введите параметр в формате --%s Значение' % arg_name)
        exit(1)


def load_data(filepath: str):
    with open(filepath, mode='r', encoding="utf-8") as file:
        return json.load(file)


def get_biggest_bar(data):
    return max(data, key=lambda el: el['Cells']['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda el: el['Cells']['SeatsCount'])


def get_closest_bar(data, longitude: float, latitude: float):
    return min(data, key=lambda el: math.sqrt(
        (el['Cells']['geoData']['coordinates'][0] - longitude)**2 +
        (el['Cells']['geoData']['coordinates'][1] - latitude)**2))


if __name__ == '__main__':

    file_path = get_named_argument('json')
    if os.path.isfile(file_path):
        try:
            data = load_data(file_path)
        except PermissionError:
            print('У вас нет прав доступа к файлу')
            exit(1)
    else:
        print('Файл не найден')
        exit(1)

    latitude = float(input('Введите широту вашего местоположения: '))
    longitude = float(input('Введите долготу вашего местоположения: '))

    if platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()

    print('Бар с мин. кол-вом мест:\n', get_smallest_bar(data), '\n')
    print('Бар с макс. кол-вом мест:\n', get_biggest_bar(data), '\n')
    print('Самый близкий бар:\n', get_closest_bar(data, longitude, latitude),
          '\n')
