from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class ReadingLog(models.Model):
    CURRENTLY_READING = 'CR'
    TO_READ = 'TR'
    HAVE_READ = 'HR'
    STATUS_CHOICES = [
        (CURRENTLY_READING, 'Currently Reading'),
        (TO_READ, 'To Read'),
        (HAVE_READ, 'Have Read')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=HAVE_READ)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bt_reading_log'
