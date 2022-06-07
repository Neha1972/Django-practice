from django.db import models


# Create your models here.
class CarItem(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


