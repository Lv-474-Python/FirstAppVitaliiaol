from django import forms
from django.core.validators import RegexValidator
from django.forms import PasswordInput, ValidationError, TextInput
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=25,
                               validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')],
                               widget=TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(min_length=9, max_length=125, widget=PasswordInput(attrs={"class": "form-control"}))
    re_password = forms.CharField(min_length=9, max_length=125, widget=PasswordInput(attrs={"class":"form-control"}),
                                  label='Confirm your password')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

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
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            raise ValidationError('Unfortunately, this username is taken')
        except User.DoesNotExist:
            return username


class SignInForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        fields = ['username', 'password']