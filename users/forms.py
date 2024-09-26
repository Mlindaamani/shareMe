from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


# User-Registration-Form

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, max_length=254, error_messages={
            'empty_field': "Email is required"
        })
# Remove helper text

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# User-login-Form

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

# Update Profile Form


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None

    class Meta:
        model = Profile
        fields = ['image', 'phone_number', 'married', 'gender']
