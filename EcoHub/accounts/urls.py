from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from .views import (
    CustomLoginView, RegisterView, MyProductsView,
    MyProfileView, ManageProductsView, ProfileUpdateView, DeleteProductView
)
from ..products.views import ProductCreateView
from .views import ResetPasswordView, SetNewPasswordView

urlpatterns = [
    #
    path('login/', CustomLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),

    path('my-profile/', MyProfileView.as_view(), name='my_profile'),
    path('update-profile-picture/', ProfileUpdateView.as_view(), {'field': 'profile_picture'},
         name='update_profile_picture'),
    path('update-email/', ProfileUpdateView.as_view(), {'field': 'email'}, name='update_email'),
    path('update-phone/', ProfileUpdateView.as_view(), {'field': 'phone'}, name='update_phone'),
    path('update-address/', ProfileUpdateView.as_view(), {'field': 'address'}, name='update_address'),
    path('update-about/', ProfileUpdateView.as_view(), {'field': 'about'}, name='update_about'),

    path('add-product/', ProductCreateView.as_view(), name='add_product'),
    path('delete-product/<int:product_id>/', DeleteProductView.as_view(), name='delete_product'),
    path('my-products/', MyProductsView.as_view(), name='my_products'),
    path('manage-products/', ManageProductsView.as_view(), name='manage_products'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/', SetNewPasswordView.as_view(), name='password_reset_confirm'),
]
