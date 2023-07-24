from django.views import View
from django.shortcuts import render, redirect
from store.models.user import User_Profile
from django.contrib.auth.hashers import check_password
from django.contrib import messages


class Signin(View):
    """ The login class view """

    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = User_Profile.get_user_by_email(email)

            if user:
                password_check = check_password(password, user.password)
                if password_check:
                    request.session['user'] = user.id
                    return redirect('/')
            else:
                messages.info(request, 'Email or Password incorrect!!!')
                return redirect('signin')
        else:
            return render(request, 'signin.html')


def logout(request):
    request.session.clear()
    return redirect('signin')