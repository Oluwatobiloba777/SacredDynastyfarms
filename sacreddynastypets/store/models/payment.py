# from django.db import models
# from .order import Order
#
#
# class Payment(models.Model):
#     """ the payment class model"""
#     order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     payment_date = models.DateTimeField()
#     payment_method = models.CharField()