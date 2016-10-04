# -*- coding: utf-8 -*-
import json
import win_unicode_console
import math


def load_data(filepath):
    with open(filepath, mode='r', encoding="utf-8") as file:
        return json.load(file)


def get_biggest_bar(data):
    return max(data, key=lambda el: el['Cells']['SeatsCount'])


def get_smallest_bar(data) -> list:
    return min(data, key=lambda el: el['Cells']['SeatsCount'])


def get_closest_bar(data, longitude, latitude) -> list:
    return min(data, key=lambda el: math.sqrt((el['Cells']['geoData']['coordinates'][0] - longitude)**2 +
                                              (el['Cells']['geoData']['coordinates'][1] - latitude)**2))


if __name__ == '__main__':
    latitude = float(input('Введите широту вашего местоположения:'))
    longitude = float(input('Введите долготу вашего местоположения:'))

    data = load_data('Бары.json')

    win_unicode_console.enable()

    print('Бар с минимальным количеством мест:\n', get_smallest_bar(data), '\n')
    print('Бар с максимальным количеством мест:\n', get_biggest_bar(data), '\n')
    print('Самый близкий бар:\n', get_closest_bar(data, longitude, latitude), '\n')

'''
Json file item example
{
    "Id":"ae3e9479-070f-4d66-9429-de3acd8427ac",
    "Number":1,
    "Cells":{
        "global_id":20660594,
        "Name":"Юнион Джек",
        "IsNetObject":"нет",
        "OperatingCompany":null,
        "AdmArea":"Центральный административный округ",
        "District":"Мещанский район",
        "Address":"Нижний Кисельный переулок, дом 3, строение 1",
        "PublicPhone":[{"PublicPhone":"(495) 621-19-63"}],
        "SeatsCount":30,
        "SocialPrivileges":"нет",
        "geoData":{
            "type":"Point",
            "coordinates":[37.621587946152012,55.765366956608361]
        }
    }
},
'''