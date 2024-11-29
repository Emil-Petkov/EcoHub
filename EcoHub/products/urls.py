from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('shop-detail/', views.shop_detail, name='shop_detail'),

    path('add/', views.add_product, name='add_product')
]
