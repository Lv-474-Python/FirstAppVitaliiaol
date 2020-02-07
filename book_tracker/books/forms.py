from django import forms
from django.forms import TextInput, Textarea, NumberInput, DateInput, Select, SelectMultiple
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
            'authors': SelectMultiple(attrs={"class": "form-control"})
        }

    def clean(self):
        super(AddBookForm, self).clean()
        title = self.cleaned_data.get('title')

        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError("Looks like we've already got a book with that title!")

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].queryset = Author.objects.order_by('last_name')


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

        help_texts = {
            'date_of_birth': "Please, input the date like this: YYYY-MM-DD"
        }

    def clean(self):
        super(AddAuthorForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError('We already have that author in our database!')


class BookSearchForm(forms.Form):
    GENRE_CHOICES = [
        ('', 'Choose genre'),
        ('NF', 'Non-Fiction'),
        ('PT', 'Poetry'),
        ('NV', 'Novel'),
        ('AN', 'Anthology'),
        ('PL', 'Play')
    ]

    by_title = forms.CharField(widget=TextInput(attrs={"class": "form-control", "placeholder": "Search by title..."}))
    by_author = forms.CharField(widget=TextInput(attrs={"class": "form-control", "placeholder": "Search by author..."}))
    by_genre = forms.ChoiceField(choices=GENRE_CHOICES, initial='', widget=Select(attrs={"class": "form-control"}))

    class Meta:
        fields = ['by_title', 'by_author', 'by_genre']

    def __init__(self, *args, **kwargs):
        super(BookSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False
