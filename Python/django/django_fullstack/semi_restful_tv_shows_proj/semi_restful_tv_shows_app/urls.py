from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='home'),
    path('shows', views.index, name='shows'),
    path('shows/new', views.new_show, name='new_show'),
    path('shows/create', views.create, name='create'),
    path('shows/<int:tv_show_id>', views.tv_show, name='tv_show'),
    path('shows/<int:tv_show_id>/edit', views.edit, name='edit'),
    path('shows/<int:tv_show_id>/update', views.update, name='update'),
    path('shows/<int:tv_show_id>/destroy', views.destroy, name='destroy'),
]
