# Решение задачи [№3](https://devman.org/challenges/3/) с сайта [devman.org](https://devman.org)

## Условие задачи:

На сайте [data.mos.ru](http://data.mos.ru) есть много разных данных, 
в том числе список московских баров.

Требуется скачать его в формате json и написать скрипт, 
который рассчитает:

Самый большой бар;
Самый маленький бар;
Самый близкий бар (текущие gps-координаты ввести с клавиатуры).

Пример json-файла (обратите внимание, в координатах сначала идёт 
долгота, затем широта:

```json
[
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
]
```

## Системные требования

```
Python 3.5.2+
Внешний модуль requests
Внешний модуль win-unicode-console
Внешний модуль geopy
```

## Установка

Windows

```    
git clone https://github.com/ram0973/3_bars.git
cd 3_bars
pip install -r requirements.txt
```

Linux
```    
git clone https://github.com/ram0973/3_bars.git
cd 3_bars
pip3 install -r requirements.txt
```
    
    
## Описание работы
Пользователь вводит свои координаты с клавиатуры. Скрипт загружает 
данные с сервера, распаковывает данные из zip-архива и выводит
данные по самому большому бару, самому маленькому бару, самому близкому 
бару.
Расстояние вычисляется по формуле отсюда:
http://gis-lab.info/qa/great-circles.html   
    
## Настройки

Если нужно, изменить константу JSON_FILE_URL, в которой хранится 
URL файла с данными о барах, в файле bars.py

## Запуск

Windows

python bars.py
 
Linux
 
python3 bars.py 

## Тесты

```
Windows: python tests.py
Linux: python3 tests.py
```
    
## Лицензия

[MIT](http://opensource.org/licenses/MIT)