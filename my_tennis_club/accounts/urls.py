from django.urls import path
from .views import sign_up
from . import views

urlpatterns = [
    path('signup/', views.signup , name='sign_up'),
]