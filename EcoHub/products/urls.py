from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('detail/', views.shop_detail, name='shop_detail'),
]
