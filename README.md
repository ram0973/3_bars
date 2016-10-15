# Решение задачи №3 с сайта [devman.org](http://devman.org)

## Условие задачи:

На сайте [data.mos.ru](http://data.mos.ru) есть много разных данных, 
в том числе список московских баров.

Требуется скачать его в формате json и написать скрипт, который рассчитает:

самый большой бар;
самый маленький бар;
самый близкий бар (текущие gps-координаты ввести с клавиатуры).

Пример json-файла:

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

## Требования

```
Python 3.5
Внешний модуль requests
Внешний модуль win-unicode-console
```

## Установка

```    
git clone https://github.com/ram0973/3_bars.git
cd 3_bars
pip install -r requirements.txt
```
    
## Настройки

Если нужно, изменить константу JSON_URL, в которой хранится URL файла с данными о 
барах, в файле bars.py

## Запуск

python bars.py 
    
## Лицензия

[MIT](http://opensource.org/licenses/MIT)