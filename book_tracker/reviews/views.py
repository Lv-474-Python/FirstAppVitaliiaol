from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from books.models import Book
from .forms import AddReview
from reading_log.models import ReadingLog
from reviews.models import Review


@login_required(login_url='signin')
def add_review(request, slug):
    book = Book.objects.get(slug=slug)
    user = request.user
    try:
        rl = user.readinglog_set.get(book=book)
        if not rl.status == 'HR':
            rl.status = 'HR'
            rl.save()
    except ReadingLog.DoesNotExist:
        rl = ReadingLog.objects.create(user=user, book=book, status='HR')
    if request.method == "POST":
        form = AddReview(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.book = book
            form.save()
            return redirect('home')
    else:
        form = AddReview()
    return render(request, 'reviews/add_review.html', {'form': form, 'book': book})


'''@login_required(login_url='signin')
def update_review(request, slug):
    book = Book.objects.get(slug=slug)
    user = request.user
    if request.method == "POST":
        form = AddReview(request.POST, instance=user.review_set.get(book=book))
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddReview()
    return render(request, 'reviews/update_review.html', {'form': form, 'book': book})'''
