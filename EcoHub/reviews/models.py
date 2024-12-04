from django.conf import settings
from django.db import models


class Review(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    comment = models.TextField()
    satisfaction = models.PositiveIntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
