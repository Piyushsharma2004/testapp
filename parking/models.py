from django.db import models

# Create your models here.
class car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    