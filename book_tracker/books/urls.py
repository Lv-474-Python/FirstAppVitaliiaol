from django.urls import path
from .views import add_book, add_author, display_books, view_book

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('add_author/', add_author, name="add_author"),
    path('display_books', display_books, name='display_books'),
    path('<int:book_id>', view_book, name='view_book')
]
