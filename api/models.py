from django.db import models

# Create your models here.
# Tablas de la DB
class CartItem(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} - {self.product_price} - {self.product_quantity}"