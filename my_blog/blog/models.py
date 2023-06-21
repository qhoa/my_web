from django.db import models
from django.contrib import auth
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
    )
    #body = models.TextField()
    #body = RichTextField()
    body = RichTextUploadingField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
#        return reverse('home')
        return  reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    def __str__(self):
        return self.comment