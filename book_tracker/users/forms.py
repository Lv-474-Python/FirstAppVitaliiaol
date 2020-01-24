from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=75, help_text='Enter your first name')
    last_name = forms.CharField(max_length=75, help_text='Enter your last name')
    email = forms.EmailField(max_length=200, required=True, help_text='Enter your email')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
        }