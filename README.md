# ������ �3 � ����� devman.org

�� ����� data.mos.ru ���� ����� ������ ������, 
� ��� ����� ������ ���������� �����.

��������� ������� ��� � ������� json � �������� ������, ������� ����������:

����� ������� ���;
����� ��������� ���;
����� ������� ��� (������� gps-���������� ������ � ����������).

������ json-�����:

```json
[
    {
        "Id":"ae3e9479-070f-4d66-9429-de3acd8427ac",
        "Number":1,
        "Cells":{
            "global_id":20660594,
            "Name":"����� ����",
            "IsNetObject":"���",
            "OperatingCompany":null,
            "AdmArea":"����������� ���������������� �����",
            "District":"��������� �����",
            "Address":"������ ��������� ��������, ��� 3, �������� 1",
            "PublicPhone":[{"PublicPhone":"(495) 621-19-63"}],
            "SeatsCount":30,
            "SocialPrivileges":"���",
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

## ������ Python : 3.5

## ���������

    pip install -r requirements.txt
    
## �������������
    
    
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