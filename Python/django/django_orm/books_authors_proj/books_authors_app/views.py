from django.shortcuts import render, redirect
from .models import Book, Author


def index(request):
    return render(request, 'index.html')


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        authors = request.POST.getlist('authors')
        book = Book.objects.create(title=title, desc=desc)
        book.authors.set(authors)
        return redirect('books')
    else:
        authors = Author.objects.all()
        return render(request, 'create_book.html', {'authors': authors})


def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'view_book.html', {'book': book})


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        authors = request.POST.getlist('authors')
        book.title = title
        book.desc = desc
        book.authors.set(authors)
        book.save()
        return redirect('view-book', book_id=book_id)
    else:
        authors = Author.objects.all()
        context = {'book': book, 'authors': authors}
        return render(request, 'edit_book.html', context)


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'delete_book.html', {'book': book})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})


def create_author(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        author = Author.objects.create(
            first_name=first_name, last_name=last_name)
        return redirect('authors')
    else:
        books = Book.objects.all()
        return render(request, 'create_author.html', {'books': books})


def view_author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.books.all()
    available_books = Book.objects.exclude(authors__id=author_id)
    if request.method == 'POST':
        book_id = request.POST.get('book')
        if book_id:
            book = Book.objects.get(id=book_id)
            author.books.add(book)
            return redirect('view-author', author_id=author_id)
    context = {'author': author, 'books': books,
               'available_books': available_books}
    return render(request, 'view_author.html', context)


def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.all()  # Retrieve all books

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        selected_books = request.POST.getlist(
            'books')  # Retrieve the selected books

        author.first_name = first_name
        author.last_name = last_name
        # Update the author's books relationship
        author.books.set(selected_books)
        author.save()

        return redirect('view-author', author_id=author_id)

    return render(request, 'edit_author.html',
                  {'author': author, 'books': books})


def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('authors')
    else:
        return render(request, 'delete_author.html', {'author': author})
