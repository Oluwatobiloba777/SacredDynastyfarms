from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile
from store.models.product import Products


class Products_Details(View):
    """Product Details Class View """

    def get(self, request, pk):
        products = Products.objects.get(pk=pk)
        return render(request, 'products-details.html', locals())

    def post(self, request):
        return render(request, 'products-details.html')
