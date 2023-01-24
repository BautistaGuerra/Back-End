from django.db import models

# Create your models here.

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name