from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Product(models.Model):
    PRICE_UNIT_CHOICES = [
        ('kg', 'Per Kilogram'),
        ('item', 'Per Item'),
        ('liter', 'Per Liter'),
        ('jar', 'Per Jar'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(
        max_length=10,
        choices=PRICE_UNIT_CHOICES,
        default='kg'
    )
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
