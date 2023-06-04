from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [ 
    path('members/',views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('register/', views.register),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)