from django.shortcuts import render, redirect
from .models import Dojo, Ninja


def dojos(request):
    dojos = Dojo.objects.all()
    return render(request, 'index.html', {'dojos': dojos})


def create_dojo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        desc = request.POST.get('desc')
        Dojo.objects.create(name=name, city=city, state=state, desc=desc)
    return redirect('dojos')


def create_ninja(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dojo_id = request.POST.get('dojo')
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(first_name=first_name,
                             last_name=last_name, dojo=dojo)
    return redirect('dojos')


def delete_dojo(request, dojo_id):
    if request.method == 'POST':
        dojo = Dojo.objects.get(id=dojo_id)
        dojo.ninjas.all().delete()  # Delete all associated ninjas
        dojo.delete()  # Delete the dojo
    return redirect('dojos')


def delete_ninja(request, ninja_id):
    if request.method == 'POST':
        ninja = Ninja.objects.get(id=ninja_id)
        ninja.delete()  # Delete the ninja
    return redirect('dojos')
