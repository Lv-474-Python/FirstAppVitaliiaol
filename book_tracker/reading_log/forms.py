from .models import ReadingLog
from books.models import Book
from django.contrib.auth.models import User
from django import forms


class AddBookToLog(forms.ModelForm):

    class Meta:
        model = ReadingLog
        exclude = ['user']
        
    
