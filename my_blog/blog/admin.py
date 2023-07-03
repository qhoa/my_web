from django.contrib import admin
from .models import Post, Comment, Category, SubCategory, User

class MenuPostAdmin(admin.ModelAdmin):
    list_display = ['title']

class MenuCommentAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Post, MenuPostAdmin)
admin.site.register(Comment, MenuCommentAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(User)
