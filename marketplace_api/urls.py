from django.urls import path
from .views import (
    ProductAPIView, StoreListCreateAPIView, EditProductAPIView,
)

app_name = 'marketplace_api'
urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products-edit/<str:id>/', EditProductAPIView.as_view(), name='products_edit'),
    path('stores/', StoreListCreateAPIView.as_view(), name='stores'),
]