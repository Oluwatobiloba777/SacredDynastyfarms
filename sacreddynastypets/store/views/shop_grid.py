from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile
from store.models.product import Products


class Shop_Grid(View):
    """Shop Grid Class View """

    def get(self, request, category):
        products = Products.objects.filter(category=category)
        content = {'category': category, 'products': products}
        # title = Products.objects.filter(category=val).values('title')
        return render(request, 'shop-grid.html', content)

    def post(self, request):
        return render(request, 'shop-grid.html')