from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput

from users.models import UserProfile


class EditUserInfo(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=self.instance.username).exists():
            raise forms.ValidationError('This email address is already in use')
        return email


class EditUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about', 'location', 'website', 'hide_email']
        widgets = {
            'about': forms.Textarea(attrs={"class": "form-control"}),
            'location': forms.TextInput(attrs={"class": "form-control"}),
            'website': forms.URLInput(attrs={"class": "form-control"}),
            'hide_email': forms.CheckboxInput(attrs={"class": "form-control"})
        }

        def __init__(self, *args, **kwargs):
            super(EditUserProfile, self).__init__(*args, **kwargs)
            for field in self.fields:
                field.required = False


class ChangeUserPassword(forms.Form):
    old_password_correct = True
    old_password = forms.CharField(min_length=9, max_length=25, widget=PasswordInput(attrs={"class": "form-control"}))
    new_password = forms.CharField(min_length=9, max_length=25, widget=PasswordInput(attrs={"class": "form-control"}))
    re_password = forms.CharField(min_length=9, max_length=25, widget=PasswordInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super(ChangeUserPassword, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    class Meta:
        fields = ['old_password', 'new_password', 're_password']

        labels = {
            'old_password': "Enter your current password",
            'new_password': "Your new password",
            're_password': "Confirm new password",
        }

    def flag_old_password(self):
        self.old_password_correct = False
        return 0

    def clean_old_password(self):
        if not self.old_password_correct:
            raise forms.ValidationError('The password you entered is incorrect')

    def clean(self):
        super(ChangeUserPassword, self).clean()
        new_password = self.cleaned_data.get('new_password')
        re_password = self.cleaned_data.get('re_password')
        old_password = self.cleaned_data.get('old_password')
        if new_password != re_password:
            raise forms.ValidationError("Your passwords don't match")
        if new_password == old_password:
            raise forms.ValidationError("You can't repeat your old password")
        return self.cleaned_data
