from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Contact(View):
    """Contact Class View """

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'contact.html', {'user': user.username})