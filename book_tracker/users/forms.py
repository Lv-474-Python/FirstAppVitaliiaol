from django import forms
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator
from django.forms import PasswordInput, ValidationError, TextInput, EmailInput
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=25, validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
    email = forms.EmailField()
    password = forms.CharField(min_length=9, max_length=125)
    re_password = forms.CharField(min_length=9, max_length=125, label='Confirm your password')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
        self.fields['username'].widget = TextInput(attrs={"class": "form-control"})
        self.fields['email'].widget = EmailInput(attrs={"class": "form-control"})
        self.fields['password'].widget = PasswordInput(attrs={"class": "form-control"})
        self.fields['re_password'].widget = PasswordInput(attrs={"class": "form-control"})

    class Meta:
        fields = ['username', 'email', 'password', 're_password']

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if not password == re_password:
            raise ValidationError("Passwords don't match")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("Looks like somebody's already using this email address")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Unfortunately, this username is taken')
        except User.DoesNotExist:
            return username


class SignInForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        fields = ['username', 'password']

    def check_user(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return user
        else:
            raise ValidationError('Invalid login or password. Please, try again!')

    def clean(self):
        super(SignInForm, self).clean()
        self.check_user()
        return self.cleaned_data
