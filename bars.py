# -*- coding: utf-8 -*-
import json
import win_unicode_console
import math

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


def load_data(filepath):
    pass


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    pass




def calc_distance(llat1, llong1, llong2, llat2):
    # http://gis-lab.info/qa/great-circles.html
    #pi - число pi, rad - радиус сферы (Земли)
    rad = 6372795

    #в радианах
    lat1 = llat1*math.pi/180.
    lat2 = llat2*math.pi/180.
    long1 = llong1*math.pi/180.
    long2 = llong2*math.pi/180.

    #косинусы и синусы широт и разницы долгот
    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)
    delta = long2 - long1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)

    #вычисления длины большого круга
    y = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
    x = sl1*sl2+cl1*cl2*cdelta
    ad = math.atan2(y, x)
    dist = ad*rad

    return dist


my_lat = float(input('Введите широту вашего местоположения:'))
my_long = float(input('Введите долготу вашего местоположения:'))


with open('Бары.json', mode='rt', encoding="utf-8", errors="surrogateescape") as file:
    parsed_data = json.load(file)

    max_seats_saloon = {}
    min_seats_saloon = {}
    min_distance_saloon = {}
    max_seats = parsed_data[0]['Cells']['SeatsCount']
    min_seats = parsed_data[0]['Cells']['SeatsCount']
    coords = parsed_data[0]['Cells']['geoData']['coordinates']
    min_distance = calc_distance(my_lat, my_long, coords[1], coords[0])

    for counter in range(len(parsed_data)):
        seats = parsed_data[counter]['Cells']['SeatsCount']
        coords = parsed_data[counter]['Cells']['geoData']['coordinates']
        # сначала долгота, потом широта в json
        distance = calc_distance(my_lat, my_long, coords[1], coords[0])
        if seats >= max_seats:
            max_seats = seats
            max_seats_saloon = parsed_data[counter]
        if seats <= min_seats:
            min_seats = seats
            min_seats_saloon = parsed_data[counter]
        if distance <= min_distance:
            min_distance = distance
            min_distance_saloon = parsed_data[counter]

win_unicode_console.enable()
print('Бар с минимальным количество мест:')
print(min_seats_saloon)
print()
print('Бар с максимальным количество мест:')
print(max_seats_saloon)
print()
print('Самый близкий бар:\n')
print(min_distance_saloon)

print()

