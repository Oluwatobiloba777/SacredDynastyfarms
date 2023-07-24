from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile
from store.models.product import Products
from store.models.user import User_Profile


class Index(View):
    """ the index class based view"""
## i'm trying to create a link for the products banner
    def get(self, request):
        products = Products.objects.all()
        users = User_Profile.get_user_by_username
        return render(request, 'index.html', locals())

    def post(self, request):
        return render(request, 'index.html')



"""
    for the contact page
    1. use the form to post the data to the db contact us
    2. create a success page
    3.

"""