from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Terms_Conditions(View):
    """Term and Conditions Class View """

    def get(self, request):
        return render(request, 'terms-conditions.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'terms-conditions.html', {'user': user.username})