from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from books.models import Book
from reviews.models import Review
from .forms import AddBookToLog
from .models import ReadingLog
from django.http import JsonResponse


@login_required(login_url='signin')
def add_to_log(request, slug):
    book = Book.objects.get(slug=slug)
    user = request.user
    instance = AddBookToLog.get_instance(user, book)
    if request.method == "POST":
        form = AddBookToLog(request.POST, instance=instance)
        try:
            user.review_set.get(book=book)
            form.add_error(None, "Couldn't change the status, you must delete your reviews first.")
        except Review.DoesNotExist:
            pass
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.book = book
            form.save()
            return redirect('view_book', slug=book.slug)
    else:
        form = AddBookToLog(instance=instance)
    return render(request, 'reading_log/add_to_log.html', {'form': form, 'book': book})


@login_required(login_url='signin')
def view_log(request):
    user = request.user
    logged_books = ReadingLog.objects.filter(user=user)
    context = {
        'user': user,
        'logged_books': logged_books
    }
    return render(request, 'reading_log/view_log.html', context)


@login_required(login_url='signin')
def delete_log(request, log_id):
    if request.method == "POST":
        log = ReadingLog.objects.get(id=log_id)
        try:
            review = log.user.review_set.get(book=log.book)
            review.delete()
        except Review.DoesNotExist:
            pass
        log.delete()
        response = {'success': 'OK'}
        return JsonResponse(response)

