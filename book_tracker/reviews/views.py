from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from books.models import Book
from reading_log.models import ReadingLog
from .forms import AddReview


@login_required(login_url='signin')
def add_review(request, slug):
    book = Book.objects.get(slug=slug)
    user = request.user
    try:
        reading_log = user.readinglog_set.get(book=book)
        if not reading_log.status == 'HR':
            reading_log.status = 'HR'
            reading_log.save()
    except ReadingLog.DoesNotExist:
        reading_log = ReadingLog.objects.create(user=user, book=book, status='HR')
    instance = AddReview.get_instance(user, book)
    if request.method == "POST":
        form = AddReview(request.POST, instance=instance)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.book = book
            form.save()
            return redirect('home')
    else:
        form = AddReview(instance=instance)
    return render(request, 'reviews/add_review.html', {'form': form, 'book': book})
