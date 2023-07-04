from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import register_form
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.

class sign_up(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

def signup(request):
    if request.method == 'GET':
        form = register_form()
        return render(request, 'registration/signup.html', {'form': form})
    if request.method == 'POST':
        form = register_form(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('sign_up')
        else:
            return render(request, 'registration/signup.html', {'form': form})