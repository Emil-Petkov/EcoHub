from django.urls import path
from . import views

urlpatterns = [
    path('testimonial/', views.testimonial_view, name='testimonial'),
]
