# 3학년 2학기 데이터베이스 Django 실습

## Features
아래의 기능들을 버튼을 누름으로써 수행
* categorydb에 products, pcs, laptops, printers 테이블을 생성
* 각 테이블에 하드코딩된 데이터 삽입
* 문제에 맞는 query 실행
    * Find the average hard disk size of PCs
        ```sql
        SELECT AVG(hd) FROM pcs
        ```
    * Find the average speed of laptop for each maker;
        ```sql
        SELECT maker, AVG(speed)
        FROM products NATURAL JOIN laptops
        GROUP BY maker;
        ```
    * Find the price of laptop, which is the only laptop model of the maker
        ```sql
        SELECT model, price
        FROM products NATURAL JOIN laptops
        WHERE maker IN (
            SELECT maker
            FROM products NATURAL JOIN laptops
            GROUP BY maker HAVING COUNT(model) = 1);
        ```
    * Find the model and price of the printer of the highest price of each maker
        ```sql
        SELECT printers.model, price
        FROM products, printers
        WHERE products.model = printers.model AND price IN (
            SELECT MAX(price)
            FROM products, printers
            WHERE products.model = printers.model
            GROUP BY maker);
        ```
* DROP TABLE

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

## How to run
[database 설정](#setting) 후에 실행 가능합니다.

### window(cmd)
```
> "projectEnv/Scripts/activate"
> python manage.py runserver
```