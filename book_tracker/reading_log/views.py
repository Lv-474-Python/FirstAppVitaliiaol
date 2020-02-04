from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from books.models import Book
from .forms import AddBookToLog
from .models import ReadingLog


@login_required(login_url='signin')
def add_to_log(request, slug):
    book = Book.objects.get(slug=slug)
    user = request.user
    instance = AddBookToLog.get_instance(user, book)
    if request.method == "POST":
        form = AddBookToLog(request.POST, instance=instance)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.book = book
            form.save()
            return redirect('home')
    form = AddBookToLog(instance=instance)
    return render(request, 'reading_log/add_to_log.html', {'form': form, 'book': book})


@login_required(login_url='signin')
def view_log(request):
    user = request.user
    logged_books = ReadingLog.objects.filter(user=user)
    context = {'user': user, 'logged_books': logged_books}
    return render(request, 'reading_log/view_log.html', context)
