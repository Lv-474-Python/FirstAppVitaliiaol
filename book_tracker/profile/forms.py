from django import forms
from users.models import UserProfile
from django.contrib.auth.models import User
from django.forms import ValidationError, PasswordInput, TextInput, Textarea, URLInput, EmailInput, CheckboxInput


class EditUserInfo(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            "first_name": TextInput(attrs={"class": "form-control"}),
            'last_name': TextInput(attrs={"class": "form-control"}),
            'email': EmailInput(attrs={"class": "form-control"})
        }
        
    def clean_email(self):
        entered_email = self.cleaned_data.get('email')
        if entered_email and User.objects.filter(email=entered_email).exclude(username=self.instance.username).exists():
            raise ValidationError('This email address is already in use')
        return entered_email


class EditUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about', 'location', 'website', 'hide_email']
        widgets = {
            'about': Textarea(attrs={"class": "form-control"}),
            'location': TextInput(attrs={"class": "form-control"}),
            'website': URLInput(attrs={"class": "form-control"}),
            'hide_email': CheckboxInput(attrs={"class": "form-control"})
        }

        def __init__(self, *args, **kwargs):
            super(EditUserProfile, self).__init__(*args, **kwargs)
            for field in self.fields:
                field.required = False


class ChangeUserPassword(forms.Form):
    old_password_correct = False
    old_password = forms.CharField(min_length=9, max_length=25, widget=PasswordInput(), label='Enter your old password')
    new_password = forms.CharField(min_length=9, max_length=25, widget=PasswordInput(), label='New password')
    re_password = forms.CharField(min_length=9, max_length=25, widget=PasswordInput(), label='Confirm new password')

    def __init__(self, *args, **kwargs):
        super(ChangeUserPassword, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    class Meta:
        fields = ['old_password', 'new_password', 're_password']

    def flag_old_password(self):
        self.old_password_correct = False
        return 0

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.old_password_correct:
            raise ValidationError('The password you entered is incorrect')
        return old_password

    def clean(self):
        super(ChangeUserPassword, self).clean()
        new_password = self.cleaned_data.get('new_password')
        re_password = self.cleaned_data.get('re_password')
        old_password = self.cleaned_data.get('old_password')
        if new_password != re_password:
            raise ValidationError("Your passwords don't match")
        elif new_password == old_password:
            raise ValidationError("You can't repeat your old password")
        return self.cleaned_data
