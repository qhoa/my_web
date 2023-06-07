from django.urls import path
from blog import views
from .views import post_new, post_delete, post_update

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>',views.post_detail, name='post_detail'),
    path('post/new', post_new.as_view(), name='post_new'),
    path('post/<int:pk>/update/', post_update.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', post_delete.as_view(), name='post_delete'),
]