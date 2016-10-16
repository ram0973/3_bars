# -*- coding: utf-8 -*-
import json
import math
import os
import zipfile
import requests
import sys

JSON_URL = 'http://data.mos.ru/opendata/export/1796/json/2/1'
ZIPPED_BARS_FILE = 'bars.zip'  # это же имя прописать в gitignore


def load_zipped_json_bars_file_from_url(url: str) -> list:
    response = requests.get(url, stream=True)
    with open(ZIPPED_BARS_FILE, 'wb') as zipped_json_bars_file:
        zipped_json_bars_file.write(response.content)
    with zipfile.ZipFile(ZIPPED_BARS_FILE) as zipped_json_bars_file:
        with zipped_json_bars_file.open(zipped_json_bars_file.namelist()[0]) \
                as json_bars_file:
            return json.loads(json_bars_file.read().decode('utf-8'))


def print_bar_info(json_bar):
    print('Название: ', json_bar['Cells']['Name'])
    print('Адрес: ', json_bar['Cells']['Address'])
    print('Телефон: ', json_bar['Cells']['PublicPhone'][0]['PublicPhone'])
    print('Количество мест: ', json_bar['Cells']['SeatsCount'])
    print('Координаты: ', json_bar['Cells']['geoData']['coordinates'])
    print('Расстояние: ', '!!!')


def get_biggest_bar(json_bars: list):
    return max(json_bars, key=lambda el: el['Cells']['SeatsCount'])


def get_smallest_bar(json_bars: list):
    return min(json_bars, key=lambda el: el['Cells']['SeatsCount'])


def get_closest_bar(json_bars: list, longitude: float, latitude: float):
    return min(json_bars, key=lambda el: math.sqrt(
        (el['Cells']['geoData']['coordinates'][0] - longitude)**2 +
        (el['Cells']['geoData']['coordinates'][1] - latitude)**2))


def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


if __name__ == '__main__':

    print('Загружаем информацию о барах...\n')
    json_bars_list = load_zipped_json_bars_file_from_url(JSON_URL)
    os.remove(ZIPPED_BARS_FILE)  # удаляем файл, чтобы не попал в git

    user_latitude = float(input('Введите широту вашего местоположения: '))
    user_longitude = float(input('Введите долготу вашего местоположения: '))

    smallest_bar = get_smallest_bar(json_bars_list)
    biggest_bar = get_biggest_bar(json_bars_list)
    closest_bar = get_closest_bar(json_bars_list,
                                  user_longitude,
                                  user_latitude)

    load_win_unicode_console()
    print('\nБар с мин. кол-вом мест:')
    print_bar_info(smallest_bar)
    print('\nБар с макс. кол-вом мест:')
    print_bar_info(biggest_bar)
    print('\nСамый близкий бар:')
    print_bar_info(closest_bar)
