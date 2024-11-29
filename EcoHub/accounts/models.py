from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_bulgarian_phone, validate_username_length


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=15,
        unique=True,
        validators=[validate_username_length],
        error_messages={
            'unique': "A user with this username already exists.",
        }
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[validate_bulgarian_phone]
    )
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
