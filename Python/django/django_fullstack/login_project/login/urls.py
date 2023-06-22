from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_registration, name='login_registration'),
    path('success', views.success, name='success'),
    path('logout', views.logout, name='logout'),
]
