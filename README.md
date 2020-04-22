# it-thematic

500 ошибка приходит в следующем виде:
====================================
DataError at /ikpz-upload-scripts/ugeoapi/api/v1/ugeoapi/providers/4/features/
ОШИБКА:  значение не умещается в тип character varying(50)


Request Method: POST
Request URL: http://dev.it-thematic.ru/ikpz-upload-scripts/ugeoapi/api/v1/ugeoapi/providers/4/features/
Django Version: 2.2.12
Python Executable: /usr/local/bin/uwsgi
Python Version: 3.6.9
Python Path: ['/usr/src/app/apps', '/usr/src/app', '.', '', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
Server time: Ср, 22 Апр 2020 06:35:18 +0000
Installed Applications:
['django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 ...
 ====================================
 Поэтому преобразование невозможно
    json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
 Тогда в бой вступает исключение на 159 строке, которое срезает строчку со словом "ОШИБКА"
 
