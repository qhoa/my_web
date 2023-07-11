from django import forms
from django.forms import ModelForm
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        #fields = ['username', 'email', 'telephone', 'password1', 'password2']
        fields = UserCreationForm.Meta.fields

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'telephone', 'avatar']

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']