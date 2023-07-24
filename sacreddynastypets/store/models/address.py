from django.db import models
from .user import User_Profile


class Address(models.Model):
    """User address class model"""
    user = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
