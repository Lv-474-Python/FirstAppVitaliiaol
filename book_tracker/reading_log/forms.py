from django import forms
from .models import ReadingLog


class AddBookToLog(forms.ModelForm):

    class Meta:
        model = ReadingLog
        fields = ['status']
        widgets = {'status': forms.Select(attrs={"class": "form-control"})}
