from django.db import models

# Create your models here.
# Create model DrinksCategory 

# Create model Drinks

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete = models.PROTECT, default=None)
    