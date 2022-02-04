from sqlite3 import Timestamp
from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=200)
    time = models.DateTimeField()
    author = models.CharField(max_length=50)

    class Meta: 
        ordering = ['-time']
