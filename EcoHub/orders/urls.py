from django.urls import path
from . import views
from .views import checkout_view


urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('delete-cart-item/<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('my-bag/', views.CartView.as_view(), name='my_bag'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout/', checkout_view, name='place_order'),

]
