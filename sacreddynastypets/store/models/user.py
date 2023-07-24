from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User_Profile(models.Model):
    """
    The customer class model
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    def register(self):
        """
        this method saves the user's information to the database
        """
        self.save()

    @staticmethod
    def email_exists(email):
        """
        Check if an email address exists in the database
        """
        return UserProfile.objects.filter(email=email).exists()

    @staticmethod
    def get_user_by_username(username):
        """
        Get a user by their username
        """
        return User_Profile.objects.filter(username=username).first()

    @staticmethod
    def get_user_by_email(email):
        """
        Get a user by their email address
        """
        return User_Profile.objects.filter(email=email).first()
