from django.db import models
from .user import User_Profile
from .orderitem import Order_Item
from .address import Address


class Order(models.Model):
    """The Order class model"""

    user = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    items = models.ManyToManyField(Order_Item)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    #payment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deliver_order = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_user_by_id(user_id):
        return Order.objects.filter(user=user_id)

