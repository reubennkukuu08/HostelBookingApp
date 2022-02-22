from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    price = models.charField(max_length = 20)
