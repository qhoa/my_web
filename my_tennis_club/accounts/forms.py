from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'password1', 'password2']

