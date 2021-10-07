from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Product, Store
from .serializers import ProductSerializer, StoreSerializer


# Create your views here.

class ProductAPIView(ListAPIView, ListCreateAPIView):
    """Отправка первых товаров магазина по критериям"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()

        seller_store = self.request.query_params.get('seller_store')
        if seller_store:
            return qs.filter(seller_store__id=seller_store)[:20]

        title = self.request.query_params.get('title')
        if title:
            return qs.filter(product_name__contains=title)

        ident = self.request.query_params.get('id')
        if ident:
            return qs.filter(id__iexact=ident)


class EditProductAPIView(UpdateAPIView, DestroyAPIView):
    """Изменение товара и его удаление"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'


class StoreListCreateAPIView(ListCreateAPIView):
    """Создание магазина"""
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

