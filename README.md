# ������� ������ [�3](https://devman.org/challenges/3/) � ����� 
[devman.org](https://devman.org)

## ������� ������:

�� ����� [data.mos.ru](http://data.mos.ru) ���� ����� ������ ������, 
� ��� ����� ������ ���������� �����.

��������� ������� ��� � ������� json � �������� ������, 
������� ����������:

����� ������� ���;
����� ��������� ���;
����� ������� ��� (������� gps-���������� ������ � ����������).

������ json-����� (�������� ��������, � ����������� ������� ��� 
�������, ����� ������:

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

## ��������� ����������

```
Python 3.5.2+
������� ������ requests
������� ������ win-unicode-console
������� ������ colorama
```

## ���������

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
    
    
## �������� ������
������������ ������ ���� ���������� � ����������. ������ ��������� 
������ � �������, ������������� ������ �� zip-������ � �������
������ �� ������ �������� ����, ������ ���������� ����, ������ �������� 
����.
���������� ����������� �� ������� ������:
http://gis-lab.info/qa/great-circles.html   
    
## ���������

���� �����, �������� ��������� JSON_FILE_URL, � ������� �������� 
URL ����� � ������� � �����, � ����� bars.py

## ������

Windows

python bars.py
 
Linux
 
python3 bars.py 

## �����

python tests.py
    
## ��������

[MIT](http://opensource.org/licenses/MIT)