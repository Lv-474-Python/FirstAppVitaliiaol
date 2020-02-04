from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddBookForm, AddAuthorForm, BookSearchForm
from .models import Book, Author


@login_required(login_url='signin')
def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_books')
    form = AddBookForm()
    context = {'form': form}
    return render(request, 'books/add_book.html', context)


@login_required(login_url='signin')
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browse_books')
    form = AddAuthorForm()
    context = {'form': form}
    return render(request, 'books/add_author.html', context)


@login_required(login_url='signin')
def display_books(request):
    books = Book.objects.all()
    #by_title_query = request.GET.get('by_title')
    #by_author_query = request.GET.get('by_author')
    if request.method == "POST":
        form = BookSearchForm(request.POST)
        by_title = form.cleaned_data.get('by_title')
        by_author = form.cleaned_data.get('by_author')

    return render(request, 'books/browse_books.html', {'books': books})


@login_required(login_url='signin')
def view_book(request, slug):
    book = Book.objects.get(slug=slug)
    authors = book.authors.all()
    return render(request, 'books/view_book.html', {'book': book, 'authors': authors})


@login_required(login_url='signin')
def view_author(request, slug):
    author = Author.objects.get(slug=slug)
    books = author.book_set.all()
    return render(request, 'books/view_author.html', {'author': author, 'books': books})
