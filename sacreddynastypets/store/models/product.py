from django.db import models
#from .category import Category

CATEGORY_CHOICES = (
    ('Dogs', 'Dog'),
    ('Cats', 'Cat'),
    ('Rabbits', 'Rabbit'),
    ('Accessories', 'Accessories'),
)


class Products(models.Model):
    """
    Product Class Model
    """

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/products/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    #create a discount field

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_products():
        """
        this method returns all products in a category
        """
        return Products.objects.all()

    @staticmethod
    def get_products_by_category(category):
        """
        this method returns products by category id
        """
        if category:
            return Products.objects.filter(category=category)
        else:
            return Products.get_all_products()