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

## ����������

```
Python 3.5
������� ������ requests
������� ������ win-unicode-console
```

## ���������

```    
git clone https://github.com/ram0973/3_bars.git
cd 3_bars
pip install -r requirements.txt
```
    
## ���������

���� �����, �������� ��������� JSON_URL, � ������� �������� URL ����� � ������� � 
�����, � ����� bars.py

## ������

python bars.py 
    
## ��������

[MIT](http://opensource.org/licenses/MIT)