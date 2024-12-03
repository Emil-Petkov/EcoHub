from django.conf import settings
from django.db import models

class Review(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    comment = models.TextField()
    satisfaction = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
