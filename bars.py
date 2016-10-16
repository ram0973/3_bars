# -*- coding: utf-8 -*-
import json
import math
import os
import zipfile
import requests
import sys
from colorama import Style


JSON_FILE_URL = 'http://data.mos.ru/opendata/export/1796/json/2/1'
ZIPPED_BARS_FILE = 'bars.zip'
# имя файла, в который загружаются данные.
# после обработки этот файл удаляется и на всякий случай он в .gitignore


def load_zipped_json_bars_file_from_url(url: str) -> list:
    """
    Загружаем данные о барах из
    """
    response = requests.get(url)
    with open(ZIPPED_BARS_FILE, 'wb') as zipped_json_bars_file:
        zipped_json_bars_file.write(response.content)
    with zipfile.ZipFile(ZIPPED_BARS_FILE) as zipped_json_bars_file:
        with zipped_json_bars_file.open(zipped_json_bars_file.namelist()[0]) \
                as json_bars_file:
            return json.loads(json_bars_file.read().decode('utf-8'))


def print_bar_info(json_bar, latitude, longitude):
    print('Название: ', json_bar['Cells']['Name'])
    print('Адрес: ', json_bar['Cells']['Address'])
    print('Телефон: ', json_bar['Cells']['PublicPhone'][0]['PublicPhone'])
    print('Количество мест: ', json_bar['Cells']['SeatsCount'])
    print('Координаты: ', json_bar['Cells']['geoData']['coordinates'])
    print('Расстояние, м: ', round(calc_distance_between_two_coordinates(
        latitude,
        longitude,
        float(json_bar['Cells']['geoData']['coordinates'][1]),
        float(json_bar['Cells']['geoData']['coordinates'][0])
    )))


def calc_distance_between_two_coordinates(llat1: float,
                                          llong1: float,
                                          llat2: float,
                                          llong2: float) -> int:
    """
    Вычисляем дистанцию между 2 коорлинатами
    http://gis-lab.info/qa/great-circles.html
    :param llat1: широта первой координаты
    :param llong1: долгота первой координаты
    :param llat2: широта второй координаты
    :param llong2: долгота второй координаты
    :return: расстояние между 2 координатами в метрах
    """

    rad = 6372795  # радиус сферы (Земли)

    # в радианах
    lat1 = llat1 * math.pi / 180.
    lat2 = llat2 * math.pi / 180.
    long1 = llong1 * math.pi / 180.
    long2 = llong2 * math.pi / 180.

    # косинусы и синусы широт и разницы долгот
    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)
    delta = long2 - long1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)

    # вычисления длины большого круга
    y = math.sqrt(math.pow(cl2 * sdelta, 2) +
                  math.pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2))
    x = sl1 * sl2+cl1*cl2*cdelta
    ad = math.atan2(y, x)
    dist = ad * rad

    return round(dist)


def get_biggest_bar(json_bars: list):
    """
    :param json_bars: список баров
    :return: бар с самым большим количество мест
    """
    return max(json_bars, key=lambda el: el['Cells']['SeatsCount'])


def get_smallest_bar(json_bars: list):
    """
    :param json_bars: список баров
    :return: бар с самым маленьким количество мест
    """
    return min(json_bars, key=lambda el: el['Cells']['SeatsCount'])


def get_closest_bar(json_bars: list, latitude: float, longitude: float):
    """
    :param json_bars: список баров
    :param latitude: широта пользователя
    :param longitude: долгота пользователя
    :return:
    """
    return min(
        json_bars,
        key=lambda el: calc_distance_between_two_coordinates(
            latitude,
            longitude,
            float(el['Cells']['geoData']['coordinates'][1]),
            float(el['Cells']['geoData']['coordinates'][0])
        )
    )


def load_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    и раскрашивание символов
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()
        from colorama import init
        #init()  # colorama


if __name__ == '__main__':

    print('Загружаем информацию о барах...\n')
    json_bars_list = load_zipped_json_bars_file_from_url(JSON_FILE_URL)
    os.remove(ZIPPED_BARS_FILE)  # прибираем мусор

    try:
        user_latitude = float(
            input('Введите широту вашего местоположения: '))
        user_longitude = float(
            input('Введите долготу вашего местоположения: '))
    except ValueError:
        print('Данные должны быть числами, например: 35.7')
        exit(1)

    smallest_bar = get_smallest_bar(json_bars_list)
    biggest_bar = get_biggest_bar(json_bars_list)
    closest_bar = get_closest_bar(json_bars_list,
                                  user_longitude,
                                  user_latitude)

    load_win_unicode_console()
    print('\n' + Style.BRIGHT + 'Бар с мин. кол-вом мест:' + Style.RESET_ALL)
    print_bar_info(smallest_bar, user_latitude, user_longitude)
    print('\n' + Style.BRIGHT + 'Бар с макс. кол-вом мест:' + Style.RESET_ALL)
    print_bar_info(biggest_bar, user_latitude, user_longitude)
    print('\n' + Style.BRIGHT + 'Самый близкий бар:' + Style.RESET_ALL)
    print_bar_info(closest_bar, user_latitude, user_longitude)
