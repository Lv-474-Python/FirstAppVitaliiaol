from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import PasswordInput

'''class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=5, validators=[RegexValidator(r'^[0-9a-zA-Z]*$',
                                                                        'Only alphanumeric characters are allowed')])
    email = forms.EmailField(max_length=200, required=True, help_text='Enter your email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
        }'''


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=25, validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
    email = forms.EmailField()
    password = forms.CharField(min_length=9, max_length=125, widget=PasswordInput())
    re_password = forms.CharField(min_length=9, max_length=125, widget=PasswordInput(), label='Confirm your password')

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
            self.add_error(re_password, "Passwords don't match")


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        fields = ['username', 'password']