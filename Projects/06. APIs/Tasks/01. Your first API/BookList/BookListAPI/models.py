from django.db import models

# Create your Book model here.
# Create Meta class inside the Book model

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
            ]
        