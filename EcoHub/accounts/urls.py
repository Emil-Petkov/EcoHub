from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from .views import (
    CustomLoginView, register_view, update_profile_picture, update_email,
    update_phone, update_address, update_about, my_products, my_profile, manage_products
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('update-profile-picture/', update_profile_picture, name='update_profile_picture'),
    path('update-email/', update_email, name='update_email'),
    path('update-phone/', update_phone, name='update_phone'),
    path('update-address/', update_address, name='update_address'),
    path('update-about/', update_about, name='update_about'),
    path('my-products/', my_products, name='my_products'),
    path('my-profile/', my_profile, name='my_profile'),
    path('manage-products/', manage_products, name='manage_products'),

    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
]
