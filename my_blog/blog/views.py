from django.shortcuts import render
from .models import Post

def home(request):
    all_post = Post.objects.all().values()
    return render(request, 'home.html', {'all_post': all_post})