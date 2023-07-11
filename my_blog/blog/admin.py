from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Post, Comment, Category, SubCategory, User

class MenuPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

class MenuCommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

#class MenuUserAdmin(admin.ModelAdmin):
#    pass
class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = UserAdmin.fieldsets + (("Extra Information", {"fields": ["age", "birthday", "telephone", "avatar"]}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Extra Information", {"fields": ["age"]}),)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    #list_display = ["username","email", "age", "is_superuser"]
    #list_filter = ["is_superuser"]
    #fieldsets = [
    #    (None, {"fields": ["username","email", "password"]}),
    #    ("Personal info", {"fields": ["age"]}),
    #    ("Permissions", {"fields": ["is_superuser"]}),
    #]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    #add_fieldsets = [
    #    (
    #        None,
    #        {
    #            "classes": ["wide"],
    #            "fields": ["username","email","age", "birthday", "password1", "password2"],
    #        },
    #    ),
    #]
    #search_fields = ["username"]
    #ordering = ["email"]
    #filter_horizontal = []


admin.site.register(Post, MenuPostAdmin)
admin.site.register(Comment, MenuCommentAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
#admin.site.register(User, UserAdmin)
admin.site.register(User, CustomUserAdmin)