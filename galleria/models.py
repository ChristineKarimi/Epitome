from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15,) 


class Location(models.Model):
    name = models.CharField(max_length=20,) 

    