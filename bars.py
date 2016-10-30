# -*- coding: utf-8 -*-
import json
import io
import requests
import sys
from zipfile import ZipFile, BadZipfile
from geopy import Nominatim
from geopy.distance import vincenty

ZIPPED_JSON_FILE_URL = 'http://data.mos.ru/opendata/export/1796/json/2/1'
REQUEST_TIMEOUT = 6  # ожидаем ответ сервера 6 секунд, для плохих соединений


def handle_requests_library_errors(decorated):
    """
    Декоратор, обрабатывающий ошибки в requests
    :param decorated: Функция, в которой надо отловить requests exceptions
    :return: декоратор
    """
    def decorator(*args, **kwargs):
        try:
            return decorated(*args, **kwargs)
        except requests.ConnectionError:
            print('Ошибка сетевого соединения')
            exit(1)
        except requests.HTTPError as e:
            print('Сервер вернул неудачный код статуса ответа: %s %i' %
                  (e.response.reason, e.response.status_code))
            exit(1)
        except requests.Timeout:
            print('Вышло время ожидания ответа от сервера')
            exit(1)
        except requests.TooManyRedirects:
            print('Слишком много редиректов')
            exit(1)

    return decorator


@handle_requests_library_errors
def download_zipped_json_bars_from(url: str) -> bytes:
    """
    Загружаем данные по барам с сервера
    :param url: адрес zip-архива с данными по барам
    :return: данные по барам полученные с сервера в виде байтов
    """
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.content


def unpack_json_bars_from(zipped_json_bars_data: bytes) -> list:
    """
    Возвращаем список баров
    :param zipped_json_bars_data: данные по барам в виде байтов
    :return: список баров
    """
    with ZipFile(io.BytesIO(zipped_json_bars_data)) as zipped_json_bars_file:
        json_bars_file_name = zipped_json_bars_file.namelist()[0]
        return json.loads(zipped_json_bars_file.read(json_bars_file_name).
                          decode('utf-8'))


def print_bar_info(json_bar, latitude: float, longitude: float):
    """
    Печатаем информацию по конкретному бару
    :param json_bar: данные по бару
    :param latitude: широта пользователя (нужна для определения расстояния)
    :param longitude: долгота пользователя (нужна для определения расстояния)
    """
    print('Название: ', json_bar['Cells']['Name'])
    print('Адрес: ', json_bar['Cells']['Address'])
    print('Телефон: ', json_bar['Cells']['PublicPhone'][0]['PublicPhone'])
    print('Количество мест: ', json_bar['Cells']['SeatsCount'])
    print('Широта: ', json_bar['Cells']['geoData']['coordinates'][1])
    print('Долгота: ', json_bar['Cells']['geoData']['coordinates'][0])

    from_point = (latitude, longitude)
    # координаты перепутаны местами в самом файле
    to_point = (float(json_bar['Cells']['geoData']['coordinates'][1]),
                float(json_bar['Cells']['geoData']['coordinates'][0]))
    print('Расстояние, км: %i' % vincenty(from_point, to_point).kilometers)


def get_biggest_bar(json_bars: list) -> dict:
    """
    Получаем самый большой бар
    :param json_bars: список баров
    :return: бар с самым большим количество мест
    """
    return max(json_bars, key=lambda el: el['Cells']['SeatsCount'])


def get_smallest_bar(json_bars: list) -> dict:
    """
    Получаем самый маленький бар
    :param json_bars: список баров
    :return: бар с самым маленьким количество мест
    """
    return min(json_bars, key=lambda el: el['Cells']['SeatsCount'])


def get_closest_bar(json_bars: list, latitude: float, longitude: float) \
        -> dict:
    """
    Получаем самый близкий к пользователю бар
    :param json_bars: список баров
    :param latitude: широта пользователя
    :param longitude: долгота пользователя
    :return: самый близкий бар
    """
    return min(
        json_bars,
        key=lambda el: vincenty(
            (latitude, longitude),
            (float(el['Cells']['geoData']['coordinates'][1]),
             float(el['Cells']['geoData']['coordinates'][0]))
        ).meters
    )


def enable_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


if __name__ == '__main__':

    print('Загружаем информацию о барах...\n')

    zipped_json_bars = download_zipped_json_bars_from(ZIPPED_JSON_FILE_URL)

    try:
        json_bars_data = unpack_json_bars_from(zipped_json_bars)
    except BadZipfile:
        print('Ошибка: неверный zip-файл c данными по барам')
        exit(1)

    try:
        user_latitude = float(
            input('Введите широту вашего местоположения: '))
        user_longitude = float(
            input('Введите долготу вашего местоположения: '))
    except ValueError:
        print('Данные должны быть числами, например: 35.7')
        exit(1)

    if abs(user_latitude) > 90. or abs(user_longitude) > 90.:
        print('Вы ввели неверные координаты')
        exit(1)

    smallest_bar = get_smallest_bar(json_bars_data)
    biggest_bar = get_biggest_bar(json_bars_data)
    closest_bar = get_closest_bar(json_bars_data,
                                  user_longitude,
                                  user_latitude)

    enable_win_unicode_console()
    geolocator = Nominatim()  # http://wiki.openstreetmap.org/wiki/Nominatim
    location = geolocator.reverse((user_latitude, user_longitude))
    print('\nВы находитесь тут: %s' % location.address)
    print('\nБар с мин. кол-вом мест:')
    print_bar_info(smallest_bar, user_latitude, user_longitude)
    print('\nБар с макс. кол-вом мест:')
    print_bar_info(biggest_bar, user_latitude, user_longitude)
    print('\nСамый близкий бар:')
    print_bar_info(closest_bar, user_latitude, user_longitude)
