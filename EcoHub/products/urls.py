from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView

urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shop'),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name='shop_detail'),
    path('add-product/', ProductCreateView.as_view(), name='add_product'),
]
