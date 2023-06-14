from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/create/', views.create_book, name='create-book'),
    path('books/<int:book_id>/', views.view_book, name='view-book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit-book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete-book'),
    path('authors/', views.authors, name='authors'),
    path('authors/create/', views.create_author, name='create-author'),
    path('authors/<int:author_id>/', views.view_author, name='view-author'),
    path('authors/<int:author_id>/edit/',
         views.edit_author, name='edit-author'),
    path('authors/<int:author_id>/delete/',
         views.delete_author, name='delete-author'),
]
