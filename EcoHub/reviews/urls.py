from django.urls import path
from . import views

urlpatterns = [
    path('testimonials/', views.testimonial, name='testimonial'),
]
