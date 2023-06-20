from django.urls import path
from blog import views
from .views import post_new, post_delete, post_update
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('post/<int:id>',views.post_detail, name='post_detail'),
    path('post/new', login_required(post_new.as_view()), name='post_new'),
    path('post/<int:pk>/update/',  post_update.as_view(), name='post_update'),
    path('post/<int:pk>/delete/',  login_required(post_delete.as_view()), name='post_delete'),    
]