# 2022년 데이터베이스 Django 프로젝트

## Setting
edit category/settings.py
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
```cmd
(cmd) "projectEnv/Scripts/activate"
(cmd) python manage.py runserver
```