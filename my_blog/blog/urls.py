from django.urls import path
from blog import views
from .views import post_delete
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('category/', views.category, name='category'),
    path('post/<int:id>',views.post_detail, name='post_detail'),
    path('post/new', login_required(views.post_new), name='post_new'),
    path('post/<int:id>/update/',  views.post_update, name='post_update'),
    path('post/<int:pk>/delete/',  login_required(post_delete.as_view()), name='post_delete'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:id>/update/', views.profile_update, name='profile_update'),
    path('account/signup', views.sign_up, name='sign_up'),
]
# Path of media files
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)