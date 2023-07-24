from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Faq(View):
    """Faq Class View """

    def get(self, request):
        return render(request, 'faq.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'faq.html', {'user': user.username})