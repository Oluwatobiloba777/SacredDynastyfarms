from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class About(View):
    """About Class View """

    def get(self, request):
        return render(request, 'about.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'contact.html', {'user': user.username})