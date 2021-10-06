# marketplace_api
api маркетплейса

Репозиторий api маркетплейса на Django 3.
Установка (для пользователей операционных систем семейства MacOs/Linux):

Открыть терминал или консоль и перейти в нужную Вам директорию
Прописать команду git clone git@gitlab.com:PyCoding1/django3-ecommerce.git

Если Вы используете https, то: git clone https://gitlab.com/PyCoding1/django3-ecommerce.git

Прописать следующие команды:


python3 -m venv ДиректорияВиртуальногоОкружения
source ДиректорияВиртуальногоОкружения/bin/activate
Перейти в директорию marketplace

pip install -r requirements.txt
python manage.py migrate


**Запустить сервер **- python manage.py runserver

**Регистрация пользователя:**
Передать POST запрос по адресу localhost:8000/api/users/
С телом запроса
```
{
    "user": {
        "username": "username",
        "email": "mail@example.com",
        "password": "password"
    }
}
```

**Вход в систему**
Передать POST запрос по адресу localhost:8000/api/users/login/
С телом запроса

{
  "user":{
    "username":"username",
    "password":"password"
  }
}

**Получение первых 20-ти товаров по названию**
Передать GET запрос по адресу localhost:8000/api/products/?title=название

**Получение товара по его id**
Передать GET запрос по адресу localhost:8000/api/products/?id=id

**Получение товаров магазина**
Передать GET запрос по адресу localhost:8000/api/products/?store_id=seller_store

**Создание товара**
Передать POST запрос по адресу localhost:8000/api/products/
С телом запроса
{
  "product_name":"название товара",
  "seller_store":"id магазина",
  "product_price":"Цена товара",
  "description":"Описание товара"
}

**Создане магазина**
Передать POST запрос по адресу localhost:8000/api/stores/
С телом запроса
{
  "store_name":"название магазина",
  "owner_id":"id владельца (id зарегистрированного пользователя)",
  "description":"Описание магазина"
}




