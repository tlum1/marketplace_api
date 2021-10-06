from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# class User(models.Model):
#     """Модель пользователя в marketplace_api"""



class Store(models.Model):
    """Модель, описывающая магазин, предоставляющий товары"""
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255, verbose_name="Название магазина")
    description = models.TextField(verbose_name="Описание магазина")

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.store_name

class Product(models.Model):
    """Модель, описывающая товар из магазина"""
    seller_store = models.ForeignKey(Store, verbose_name="Магазин", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, verbose_name="Название товара")
    product_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена товара")
    description = models.TextField(verbose_name="Описание товара")

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.product_name
