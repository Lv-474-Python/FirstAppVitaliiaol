from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddBookToLog
from books.models import Book


@login_required(login_url='signin')
def add_to_log(request, slug):
    book = Book.objects.get(slug=slug)
    if request.method == "POST":
        form = AddBookToLog(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.book = book
            form.save()
            return redirect('home')
    form = AddBookToLog()
    return render(request, 'reading_log/add_to_log.html', {'form': form, 'book': book})
