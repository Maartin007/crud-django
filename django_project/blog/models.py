from django.db import models
from django.utils import timezone

# Create your models here.

class post (models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField()
    date_posted = models.DateTimeField(default=timezone.now)