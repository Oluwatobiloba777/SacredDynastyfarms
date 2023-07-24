from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Blog_Details(View):
    """Blog Details Class View """

    def get(self, request):
        return render(request, 'blog-details.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'blog-details.html', {'user': user.username})