from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddBookForm, AddAuthorForm
from .models import Book, Author


@login_required(login_url='signin')
def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = AddBookForm()
    context = {'form': form}
    return render(request, 'add_book.html', context)


@login_required(login_url='signin')
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = AddAuthorForm()
    context = {'form': form}
    return render(request, 'add_author.html', context)


@login_required(login_url='signin')
def display_books(request):
    books = Book.objects.all()
    return render(request, 'display_books.html', {'books': books})


@login_required(login_url='signin')
def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'view_book.html', {'book': book})
