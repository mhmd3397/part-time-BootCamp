from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.


def login_registration(request):
    if request.method == 'POST':
        if 'registration_submit' in request.POST:
            registration_errors = User.objects.basic_validator_registration(
                request.POST)
            if registration_errors:
                for key, value in registration_errors.items():
                    messages.error(request, value, extra_tags='register')
                return redirect('login_registration')

            # Retrieve form data
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()

            if request.POST['birthday'] == "":
                birthday = None
            else:
                birthday = request.POST['birthday']

            # Create a new user
            user = User(first_name=first_name, last_name=last_name,
                        email=email, password=pw_hash, birthday=birthday)
            user.save()

            # Set logged-in user in the session
            request.session['user'] = {
                'first_name': user.first_name,
                'last_name': user.last_name
            }

            request.session['message'] = (
                f"Thank you, {user.first_name}"
                f" {user.last_name}, for registration!")
            return redirect('success')

        elif 'login_submit' in request.POST:
            login_errors = User.objects.basic_validator_login(request.POST)
            if login_errors:
                for key, value in login_errors.items():
                    messages.error(request, value, extra_tags='login')
                return redirect('login_registration')

            email = request.POST['email']
            user = User.objects.get(email=email)

            # Set logged-in user in the session
            request.session['user'] = {
                'first_name': user.first_name,
                'last_name': user.last_name
            }

            request.session['message'] = (
                f"Welcome back, {user.first_name} {user.last_name}!")
            return redirect('success')

    return render(request, 'login_registration.html')


def success(request):
    # Check if user is logged in
    if 'user' not in request.session:
        return redirect('login_registration')

    # Get the flash message from the session
    message = request.session.get('message')

    # Get the logged-in user
    user = request.session.get('user')

    return render(request, 'success.html', {'message': message, 'user': user})


def logout(request):
    if request.method == 'POST':
        # Check if user is logged in
        if 'user' not in request.session:
            return redirect('login_registration')
        
        # Clear the session
        request.session.flush()
    
    # Redirect to the login/registration page
    return redirect('login_registration')
