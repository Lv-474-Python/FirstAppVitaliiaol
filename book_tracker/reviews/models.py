from django.db import models
from django.contrib.auth.models import User

from books.models import Book


class Review(models.Model):
    RATING_CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(blank=True, default='')
    rating = models.CharField(choices=RATING_CHOICES, max_length=1)

    class Meta:
        db_table = 'bt_review'
