from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_bulgarian_phone, validate_username_length


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(
        max_length=15,
        unique=True,
        validators=[validate_username_length],
        error_messages={
            'unique': "A user with this username already exists.",
        }
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[validate_bulgarian_phone]
    )
    address = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
