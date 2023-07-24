from django.db import models
from .user import User_Profile
from .product import Products


class Order_Item(models.Model):
    """Order Item class model"""

    user = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def total_item_price(self):
        return self.quantity * self.product.price

