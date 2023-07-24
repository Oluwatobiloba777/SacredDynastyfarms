from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Privacy_Policy(View):
    """Privacy Policy Class View """

    def get(self, request):
        return render(request, 'privacy-policy.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'privacy-policy.html', {'user': user.username})