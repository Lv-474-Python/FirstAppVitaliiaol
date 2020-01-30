from django import forms
from django.forms import TextInput, Textarea, NumberInput, SelectMultiple, CheckboxSelectMultiple, DateInput
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
            'genre': TextInput(attrs={"class": "form-control"}),
            'authors': CheckboxSelectMultiple(attrs={"class": "form-control"})
        }

        def __init__(self, *args, **kwargs):
            super(AddBookForm, self).__init__(*args, **kwargs)
            self.fields['authors'].queryset = Author.objects.all()

        def save(self, commit=True):
            form = super(AddBookForm, self).save(commit=False)
            if commit:
                form.save()
                form.save_m2m()
            return form


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

