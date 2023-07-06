from django.db import models
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile/')

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    body = RichTextUploadingField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
#        return reverse('home')
        return  reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = RichTextField()
    def __str__(self):
        #return self.comment
        return str(self.title)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile')
    def __str__(self):
        return str(self.user.username)

