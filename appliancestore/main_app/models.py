from django.db import models

# Create your models here.
class Appliance(models.Model):
    def __init__(self, name, description, price):
        name = models.CharField(max_length=100)
        description = models.CharField(max_length=100)
        price = models.CharField(max_length=100)
