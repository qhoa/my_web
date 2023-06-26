from django.contrib import admin
from .models import Post, Comment, Category, SubCategory

class MenuPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

class MenuCommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

admin.site.register(Post, MenuPostAdmin)
admin.site.register(Comment, MenuCommentAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
