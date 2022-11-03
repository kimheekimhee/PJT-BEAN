from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile,User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "image",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']        