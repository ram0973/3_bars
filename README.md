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

## ������ Python : 3.5

## ���������

    pip install -r requirements.txt
    
## �������������
    
## ��������

[MIT](http://opensource.org/licenses/MIT)