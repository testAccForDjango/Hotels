from django.db import models
from django.conf import settings
from django.db.models.fields import IntegerField

class Hotel(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    city = models.CharField(max_length=30)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
