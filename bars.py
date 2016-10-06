# -*- coding: utf-8 -*-
import argparse
import json
import os
import math
import sys


def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def get_named_argument(arg_name: str) -> str:
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument('--' + arg_name)
        return getattr(parser.parse_args(sys.argv[1:]), arg_name)
    else:
        print('Введите параметр в формате --%s Значение' % arg_name)
        exit(1)


def load_data(filepath: str):
    if os.path.isfile(file_path):
        try:
            with open(filepath, mode='r', encoding="utf-8") as file:
                return json.load(file)
        except PermissionError:
            print('У вас нет прав доступа к файлу')
            exit(1)
    else:
        print('Файл не найден')
        exit(1)


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

    data = load_data(file_path)

    latitude = float(input('Введите широту вашего местоположения: '))
    longitude = float(input('Введите долготу вашего местоположения: '))

    load_win_unicode_console()

    print('\nБар с мин. кол-вом мест:\n', get_smallest_bar(data), '\n')
    print('Бар с макс. кол-вом мест:\n', get_biggest_bar(data), '\n')
    print('Самый близкий бар:\n', get_closest_bar(data, longitude, latitude),
          '\n')
