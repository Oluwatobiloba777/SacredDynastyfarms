from django.contrib import admin
from .models.order import Order
from .models.user import User_Profile
from .models.product import Products
from .models.address import Address
from .models.orderitem import Order_Item
#from .models.category import Category
# Register your models here.
admin.site.register(User_Profile)
admin.site.register(Order)
#admin.site.register(Products)
admin.site.register(Address)
admin.site.register(Order_Item)
#admin.site.register(Category)


@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'image', 'category']