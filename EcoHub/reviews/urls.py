from django.urls import path
from . import views

urlpatterns = [
    path('testimonial/', views.testimonial, name='testimonial'),
]
