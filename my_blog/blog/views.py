from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    all_post = Post.objects.all().values()
    return render(request, 'home.html', {'all_post': all_post})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})

class post_new(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class post_update(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']

class post_delete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
