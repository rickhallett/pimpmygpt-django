from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField("date published")
    