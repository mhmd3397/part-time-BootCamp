from django.urls import path
from . import views

urlpatterns = [
    path('', views.dojos, name='dojos'),
    path('create-dojo/', views.create_dojo, name='create-dojo'),
    path('create-ninja/', views.create_ninja, name='create-ninja'),
    path('delete-dojo/<int:dojo_id>/', views.delete_dojo, name='delete-dojo'),
    path('delete-ninja/<int:ninja_id>/',
         views.delete_ninja, name='delete-ninja'),
]
