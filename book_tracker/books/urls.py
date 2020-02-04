from django.urls import path
from .views import add_book, add_author, display_books, view_book, view_author

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('add_author/', add_author, name="add_author"),
    path('browse', display_books, name='display_books'),
    path('view_book/<slug:slug>', view_book, name='view_book'),
    path('view_author/<slug:slug>', view_author, name='view_author')
]
