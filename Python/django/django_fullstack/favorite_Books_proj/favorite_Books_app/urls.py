from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books', views.books, name='books'),
    path('books/<int:book_id>', views.view_edit_book, name='view_edit_book'),
    path('books/<int:book_id>/add_un_favorite', views.add_un_favorite, name='add_un_favorite'),  # noqa
    path('logout', views.logout, name='logout'),
]
