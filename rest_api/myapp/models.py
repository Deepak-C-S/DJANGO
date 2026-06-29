from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.TextField()
    brand=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    