from django.shortcuts import render, redirect
from .models import Tv_shows
from django.contrib import messages
# Create your views here.


def root(request):
    return redirect('/shows')


def index(request):
    context = {
        "tv_shows": Tv_shows.objects.all()
    }
    return render(request, "index.html", context)


def new_show(request):
    if request.method == 'GET':
        return render(request, 'new_show.html')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        network = request.POST.get('network')
        release_date = request.POST.get('release_date')
        desc = request.POST.get('desc')

        errors = Tv_shows.objects.basic_validator(request.POST)
        if errors:
            # If there are errors, render the form again with the errors
            for key, value in errors.items():
                messages.error(request, value)
            context = {
                'title': title,
                'network': network,
                'release_date': release_date,
                'desc': desc
            }
            return render(request, 'new_show.html', context)

        new_show = Tv_shows.objects.create(
            title=title, network=network, release_date=release_date, desc=desc)
        return redirect('tv_show', tv_show_id=new_show.id)

    return redirect('create')


def tv_show(request, tv_show_id):
    tv_show = Tv_shows.objects.get(id=tv_show_id)
    return render(request, 'tv_show.html', {'tv_show': tv_show})


def edit(request, tv_show_id):
    tv_show = Tv_shows.objects.get(id=tv_show_id)
    context = {
        'tv_show': tv_show,
        'title': tv_show.title,
        'network': tv_show.network,
        'release_date': tv_show.release_date.strftime('%Y-%m-%d'),
        'desc': tv_show.desc
    }
    return render(request, 'edit.html', context)


def update(request, tv_show_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        network = request.POST.get('network')
        release_date = request.POST.get('release_date')
        desc = request.POST.get('desc')

        errors = Tv_shows.objects.basic_validator(request.POST)
        if errors:
            # If there are errors, render the form again with the errors
            for key, value in errors.items():
                messages.error(request, value)
            context = {
                'tv_show': Tv_shows.objects.get(id=tv_show_id),
                'title': title,
                'network': network,
                'release_date': release_date,
                'desc': desc
            }
            return render(request, 'edit.html', context)

        Tv_shows.objects.filter(id=tv_show_id).update(
            title=title,
            network=network,
            release_date=release_date,
            desc=desc
        )
        return redirect('tv_show', tv_show_id=tv_show_id)

    return redirect('edit', tv_show_id=tv_show_id)


def destroy(request, tv_show_id):
    tv_show = Tv_shows.objects.get(id=tv_show_id)
    tv_show.delete()
    return redirect('home')
