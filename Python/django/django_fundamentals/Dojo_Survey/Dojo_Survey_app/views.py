from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def create_user(request):
    print("Got result Info")
    print(request.POST)
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    textarea_from_form = request.POST['textarea']
    context = {
        "name_on_template": name_from_form,
        "location_on_template": location_from_form,
        "language_on_template": language_from_form,
        "textarea_on_templates": textarea_from_form
    }
    return render(request, "results.html", context)
