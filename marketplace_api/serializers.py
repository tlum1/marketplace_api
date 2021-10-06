from rest_framework import serializers
from .models import Product, Store
from authentication.models import User


class ProductSerializer(serializers.ModelSerializer):
    """Сериализация продукта"""

    product_name = serializers.CharField(required=True)
    seller_store = serializers.CharField(required=True)
    product_price = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    seller_store = serializers.PrimaryKeyRelatedField(queryset=Store.objects)
    product_name = serializers.CharField(max_length=255)
    product_price = serializers.DecimalField(max_digits=9, decimal_places=2)
    description = serializers.CharField()

    class Meta:
        model = Product
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    """Сериализация магазина"""

    owner_id = serializers.CharField(required=True)
    store_name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    owner_id = serializers.PrimaryKeyRelatedField(queryset=User.objects)
    store_name = serializers.CharField(max_length=255)
    description = serializers.CharField()

    class Meta:
        model = Store
        fields = "__all__"
