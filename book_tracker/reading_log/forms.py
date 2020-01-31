from .models import ReadingLog
from django import forms


class AddBookToLog(forms.ModelForm):

    class Meta:
        model = ReadingLog
        exclude = ['user', 'book', 'date_updated']
        widgets = {'status': forms.Select(attrs={"class": "form-control"})}
