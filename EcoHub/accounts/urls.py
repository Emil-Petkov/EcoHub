from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('register/', TemplateView.as_view(template_name='accounts/register.html'), name='register'),

    path('my-products/', views.my_products, name='my_products'),

    path('my-profile/', views.my_profile, name='my_profile'),

    path('manage-products/', views.manage_products, name='manage_products'),
]
