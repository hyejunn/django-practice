# 2022년 데이터베이스 Django 프로젝트

## Setting
edit category/settings.py

mysql 설치 후 db에 맞게 정보 수정
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_userid',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Install
[database 설정](#setting) 후에 실행 가능합니다.
```cmd
(cmd) "projectEnv/Scripts/activate"
(cmd) python manage.py runserver
```