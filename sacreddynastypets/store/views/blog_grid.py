from django.views import View
from django.shortcuts import render
from store.models.user import User_Profile


class Blog_Grid(View):
    """Blog Grid Class View """

    def get(self, request):
        return render(request, 'blog-grid.html')

    def post(self, request):
        user = User_Profile.user_username(username)
        return render(request, 'blog-grid.html', {'user': user.username})