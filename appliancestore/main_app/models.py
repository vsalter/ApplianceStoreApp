from django.db import models

# Create your models here.
class Appliance:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


appliances = [
    Appliance('Hammer', 'Wooden', '$5.00'),
    Appliance('Hammer', 'Solid Steel', '$15.00'),
    Appliance('Screwdriver', 'Wooden Handle', '$3.00')
]