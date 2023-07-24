from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Cart(View):
    """Cart Class View """

    def get(self, request):
        return render(request, 'cart.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'cart.html', {'user': user.username})