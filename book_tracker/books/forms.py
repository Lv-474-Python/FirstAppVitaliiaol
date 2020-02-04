from django import forms
from django.forms import TextInput, Textarea, NumberInput, CheckboxSelectMultiple, DateInput
from .models import Book, Author


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = [
            'title',
            'description',
            'pages',
            'genre',
            'authors',
        ]
        widgets = {
            'title': TextInput(attrs={"class": "form-control"}),
            'description': Textarea(attrs={"class": "form-control"}),
            'pages': NumberInput(attrs={"class": "form-control"}),
            'genre': forms.Select(attrs={"class": "form-control"}),
            'authors': CheckboxSelectMultiple(attrs={"class": "form-control"})
        }

    def clean(self):
        super(AddBookForm, self).clean()
        title = self.cleaned_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError("Looks like we've already got a book with that title!")

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'first_name',
            'last_name',
            'biography',
            'date_of_birth',
        ]
        widgets = {
            'first_name': TextInput(attrs={"class": "form-control"}),
            "last_name": TextInput(attrs={"class": "form-control"}),
            "biography": Textarea(attrs={"class": "form-control"}),
            "date_of_birth": DateInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        super(AddAuthorForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError('We already have that author in our database!')


class BookSearchForm(forms.Form):

    class Meta:
        fields = ['by_title', 'by_author']

        labels = {
            'by_title': 'Search book by title',
            'by_author': 'Search book by author'
        }

        widgets = {
            'by_title': TextInput(attrs={"class": "form-control"}),
            'by_author': TextInput(attrs={"class": "form-control"})
        }

