from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Checkout(View):
    """Checkout Class View """

    def get(self, request):
        return render(request, 'checkout.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'checkout.html', {'user': user.username})