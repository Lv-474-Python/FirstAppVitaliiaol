from django import forms
from .models import ReadingLog

from reviews.models import Review


class AddBookToLog(forms.ModelForm):

    class Meta:
        model = ReadingLog
        fields = ['status']
        widgets = {'status': forms.Select(attrs={"class": "form-control"})}

    @staticmethod
    def get_instance(user, book):
        try:
            instance = user.readinglog_set.get(book=book)
        except ReadingLog.DoesNotExist:
            instance = None
        return instance
