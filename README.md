# Задача №3 с сайта devman.org

На сайте data.mos.ru есть много разных данных, 
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

[vk.com](https://vk.com) is the largest social network in Russia.
This library is significantly improved fork of [vk](https://github.com/dimka665/vk)

## Версия Python : 3.5

## Установка

    pip install -r requirements.txt
    
## Использование
    
    
## Features
### "Queryset-like" requests
    
    # Returns list of users
    api.users.get(users_ids=1)
    
    # Returns list of user's friends with extra fields 
    api.friends.get(user_id=1, fields=['nickname', 'city'])
    
    # Returns result list from your custom api method
    api.execute.YourMethod(**method_params)
 
 
## License

MIT - http://opensource.org/licenses/MIT