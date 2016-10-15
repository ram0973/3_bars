# ������� ������ �3 � ����� [devman.org](http://devman.org)

## ������� ������:

�� ����� [data.mos.ru](http://data.mos.ru) ���� ����� ������ ������, 
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
    
    git clone https://github.com/ram0973/3_bars.git
    cd 3_bars
    pip install -r requirements.txt
    
## �������������

�������� URL ����� c ������� � �����, ���� �����, � ����� bars.py:  
JSON_URL = 'http://data.mos.ru/opendata/export/1796/json/2/1'
���������: python bars.py 
    
## ��������

[MIT](http://opensource.org/licenses/MIT)