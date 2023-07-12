from django import forms
from django.forms import ModelForm
from .models import User, Post, Category, SubCategory, Comment
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

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','parent','category','body']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']