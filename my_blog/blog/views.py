from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

def home(request):
    all_post = Post.objects.all().values()
    #all_post = Post.objects.filter(title__icontains='day')
    return render(request, 'home.html', {'all_post': all_post})

def search(request):
    search_result = []
    query = request.GET.get('q')
#    if query == '':
#        query = ''
    search_result = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'search_result.html', {'search_result': search_result})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    #comment = Comment.objects.get(id=id)
    query = Comment.objects.filter(title_id=id)
    return render(request, 'post_detail.html', {'post': post, 'query': query})

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