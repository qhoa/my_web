from django.contrib import admin
from .models import Member

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date", "picture")

#class MenuImage(admin.ModelAdmin):
#    list_display = ("title", "image")

admin.site.register(Member,MenuAdmin)
#admin.site.register(Image, MenuImage)