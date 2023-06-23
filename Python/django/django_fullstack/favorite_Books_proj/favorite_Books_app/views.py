from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt
# Create your views here.


def index(request):
    if 'user' in request.session:
        return redirect('books')
    if request.method == 'POST':
        if 'registration_submit' in request.POST:
            registration_errors = User.objects.basic_validator_registration(
                request.POST)
            if registration_errors:
                for key, value in registration_errors.items():
                    messages.error(request, value, extra_tags='register')
                return redirect('home')

            # Retrieve form data
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()

            if request.POST['birthday'] == "":
                birthday = None
            else:
                birthday = request.POST['birthday']

            # Create a new user
            user = User(first_name=first_name, last_name=last_name,
                        email=email, password=pw_hash, birthday=birthday)
            user.save()

            # Set logged-in user in the session
            request.session['user'] = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'id': user.id
            }

            request.session['message'] = (
                f"Welcome, {user.first_name} {user.last_name}!")
            return redirect('books')

        elif 'login_submit' in request.POST:
            login_errors = User.objects.basic_validator_login(request.POST)
            if login_errors:
                for key, value in login_errors.items():
                    messages.error(request, value, extra_tags='login')
                return redirect('home')

            email = request.POST['email']
            user = User.objects.get(email=email)

            # Set logged-in user in the session
            request.session['user'] = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'id': user.id
            }

            request.session['message'] = (
                f"Welcome, {user.first_name} {user.last_name}!")
            return redirect('books')

    return render(request, 'login_registration.html')


def books(request):
    # Check if user is logged in
    if 'user' not in request.session:
        return redirect('home')

    # Get the flash message from the session
    message = request.session.get('message')

    # Get the logged-in user
    user = request.session.get('user')

    # Retrieve all books from the database
    books = Book.objects.all()

    if request.method == 'POST':
        form_errors = Book.objects.basic_validator(request.POST)
        if form_errors:
            for key, value in form_errors.items():
                messages.error(request, value)
            return redirect('home')
        else:
            # Create a new book
            title = request.POST['title']
            desc = request.POST['desc']
            logged_user = User.objects.get(id=user['id'])
            user = User.objects.filter(id=user['id']).first()
            book = Book(title=title, desc=desc, uploaded_by=logged_user)
            book.save()
            # Add the book to favorites for the uploader
            logged_user.fav_books.add(book)
            messages.success(request, "Book added successfully.")
            book_id = request.post['book_id']
            return redirect('books')
    existing_fav = Book.objects.get(
        id=book_id).user_who_like.filter(id=user.id)
    context = {'existing_fav': existing_fav}
    return render(request, 'books.html', {'message': message, 'user': user, 'books': books}, context)  # noqa


def add_un_favorite(request, book_id):
    # Check if user is logged in
    if 'user' not in request.session:
        return redirect('home')

    # Get the logged-in user
    user = request.session.get('user')

    # Get the book by ID
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        messages.error(request, "Book not found.")
        return redirect('books')

    # Check if the book is already favorited by the user
    user_obj = User.objects.get(id=user['id'])
    if user_obj in book.fav_users.all():
        # Book is already favorited, remove it from favorites
        user_obj.fav_books.remove(book)
        messages.success(request, f"Removed {book.title} from favorites.")
    else:
        # Book is not favorited, add it to favorites
        user_obj.fav_books.add(book)
        messages.success(request, f"Added {book.title} to favorites.")

    return redirect('books')


def view_edit_book(request, book_id):
    # Check if user is logged in
    if 'user' not in request.session:
        return redirect('home')

    # Get the logged-in user
    user = request.session.get('user')

    # Get the book by ID
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        messages.error(request, "Book not found.")
        return redirect('books')

    # Check if the logged-in user is the uploader of the book
    if user['id'] == book.uploaded_by.id:
        if request.method == 'POST':
            if 'edit_submit' in request.POST:
                # Perform book editing
                form_errors = Book.objects.basic_validator(request.POST)
                if form_errors:
                    for key, value in form_errors.items():
                        messages.error(request, value)
                    return redirect('view_edit_book', book_id)
                else:
                    # Update the book's information
                    book.title = request.POST['title']
                    book.desc = request.POST['desc']
                    book.save()
                    messages.success(request, "Book updated successfully.")
                    return redirect('view_edit_book', book_id)
            elif 'delete_submit' in request.POST:
                # Perform book deletion
                book.delete()
                messages.success(request, "Book deleted successfully.")
                return redirect('books')

        return render(request, 'edit_book.html', {'user': user, 'book': book})
    else:
        return render(request, 'view_book.html', {'user': user, 'book': book})


def logout(request):
    if request.method == 'POST':
        # Check if user is logged in
        if 'user' not in request.session:
            return redirect('home')

        # Clear the session
        request.session.flush()

    # Redirect to the login/registration page
    return redirect('home')
