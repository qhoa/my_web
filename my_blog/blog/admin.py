from django.contrib import admin
from .models import Post, Comment

class MenuPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

class MenuCommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'comment']

admin.site.register(Post, MenuPostAdmin)
admin.site.register(Comment, MenuCommentAdmin)
