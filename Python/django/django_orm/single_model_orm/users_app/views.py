from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'index.html', context)


def add_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        User.objects.create(first_name=first_name,
                            last_name=last_name, email_address=email, age=age)
        return redirect('user_list')
    return redirect('user_list')
