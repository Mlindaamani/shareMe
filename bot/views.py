from ast import arg
from audioop import reverse
from socket import inet_ntoa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpRequest
from django.contrib import messages
from .models import Book, Category, Author
from .forms import BookForm, EmailBookForm
from airdrop.settings import EMAIL_HOST_USER, MESSAGE_EMAIL


def book_list(request: HttpRequest, category_slug=None, author=None):
    category = None
    authors = Author.objects.all()
    categories = Category.objects.all()
    books = Book.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    elif author:
        author = get_object_or_404(Author, slug=author)
        books = books.filter(authors=author)
    return render(request, 'bot/book-list.html', context={'books': books, 'category': category, 'categories': categories, 'authors': authors})


def book_detail(request: HttpRequest, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'bot/book-detail.html', context={'book': book, 'form': EmailBookForm(initial={'name': request.user.username})})


@login_required
def create_book(request: HttpRequest):
    if request.method == "POST":
        form = BookForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Book '{
                             form.cleaned_data['name']}' created successfully!")
            return redirect('bot:create-book')
        else:
            return render(request, 'bot/create-book.html', context={'form', form})
    form = BookForm()
    return render(request, 'bot/create-book.html', context={"form": form})


@login_required(login_url='users:login')
def share_book(request: HttpRequest, id):

    # Retrieve a book from the database
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        form = EmailBookForm(request.POST)

        if form.is_valid():
            # Create book url for sending....
            book_url = request.build_absolute_uri(
                book.get_absolute_url()
            )

            # Get form data..........
            name = form.cleaned_data.get('name')
            to = form.cleaned_data.get('to')
            comment = form.cleaned_data.get('comment')

            # Compose an email
            subject = f"{name} recommended you a book {book.name}"
            message = MESSAGE_EMAIL.replace('BUYER', name).replace(
                'URL', book_url).replace('COMMENT', comment).replace("NAME", book.name)

            # Send email.........
            send_mail(subject, message, EMAIL_HOST_USER, [to])

            # Send a success message
            messages.success(request, f'Email sent to {name}')
            return redirect(reverse('bot:book-list'))
        return render(request, 'bot/book-detail.html', context={'form': form})
    return render(request, 'bot/book-detail.html', context={'form': EmailBookForm()})


def dashboard(request: HttpRequest):
    return render(request, 'bot/dashboard.html')
