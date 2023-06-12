from django.shortcuts import HttpResponse

# Create your views here.


def index(request):
    HttpResponse("hello")
