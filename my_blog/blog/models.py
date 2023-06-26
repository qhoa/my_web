from django.db import models
from django.contrib import auth
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 

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
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
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
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = RichTextField()
    def __str__(self):
        #return self.comment
        return str(self.title)

