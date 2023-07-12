from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category, SubCategory, User
from .forms import SignUpForm, ProfileUpdateForm, PostForm, CategoryForm
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages, auth
from django.db.models import Q

# Set global query.
all_category = Category.objects.all()
all_subcategory = SubCategory.objects.all()

def home(request):
    all_post = Post.objects.all()
    context = {
        'all_post': all_post, 
        'all_category': all_category, 
        'all_subcategory': all_subcategory
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html' ,{'all_category': all_category})

def search(request):
    search_result = []
    query = request.GET.get('q')
#    if query == '':
#        query = ''
    search_result = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'search_result.html', {'search_result': search_result})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    query = Comment.objects.filter(title_id=id)
    context = {
       'post': post, 
       'query': query, 
       'all_category': all_category,
       'all_subcategory': all_subcategory 
    }
    return render(request, 'post_detail.html', context)

def sign_up(request):
    if request.method == 'GET':
        context = {'form': SignUpForm()}
        return render(request, 'registration/sign_up.html', context)
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/sign_up.html', context)

def profile(request):
    return render(request, 'profile_detail.html')

def profile_update(request, id):
    if id != request.user.id:
        return redirect('home')
    else:
        profile = get_object_or_404(User, id=id)
        if request.method == 'GET':
            context = {'form': ProfileUpdateForm(instance=profile), 'id': id}
            return render(request,'profile_update.html', context)
        elif request.method == 'POST':
            form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            return render(request,'profile_update.html', context)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        context = {'form': PostForm()}
        return render(request, 'post_new.html', context)

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', id=id)
        else:
            context = {'form': PostForm(instance=post), 'id': id}
            return render(request, 'post_update.html', context)
    else:
        return redirect('post_detail', id=id)

#class post_update(UpdateView):
#    model = Post
#    template_name = 'post_update.html'
#    fields = ['title', 'body']

class post_delete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    



