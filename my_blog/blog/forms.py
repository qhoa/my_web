from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
#User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields