from django.shortcuts import render, redirect
from django.views import View
from store.models.user import User_Profile
from django.contrib.auth.hashers import make_password


class Signup(View):
    """The signup class view"""

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            password = request.POST['password']

            #this variable will hold the values for validation
            value = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
                'phone_number': phone_number,
                'password': password
            }

            #this populates the db with new user information
            user = User_Profile(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                phone_number=phone_number,
                password=password
            )

            error_message = self.validate_new_user(user)

            if not error_message:
                user.password = make_password(user.password)
                user.register()

                return redirect('index')
            else:
                error_data = {
                    'error': error_message,
                    'values': value
                }
                return render(request, 'signup.html', error_data)

    def validate_new_user(self, new_user):
        error_message = None
        if not new_user.first_name:
            error_message = "Please Enter your First Name!"
        elif len(new_user.first_name) < 3:
            error_message = "First Name must be 3 characters long or more!"
        elif not new_user.last_name:
            error_message = "Please Enter your Last Name!"
        elif len(new_user.last_name) < 3:
            error_message = "Last Name must be 3 characters long or more!"
        elif not new_user.username:
            error_message = "Please Enter your Username"
        elif len(new_user.username) < 3:
            error_message = "Username must be 3 characters long or more!"
        elif len(new_user.email) < 5:
            error_message = "Email Address must be 5 characters long!"
        elif new_user.user_email_exist():
            error_message = "Email Address already registered"
        elif not new_user.phone_number:
            error_message = "Enter your phone number"
        elif len(new_user.phone_number) < 9:
            error_message = "Phone number must be 10 char long"

        return error_message

