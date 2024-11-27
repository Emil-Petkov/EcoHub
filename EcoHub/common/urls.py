from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error-404/', views.error_404, name='error_404'),
]
