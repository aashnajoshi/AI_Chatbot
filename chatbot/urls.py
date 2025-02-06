from django.urls import path
from . import views
from home.views import signin, search

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('search/', search, name='search'),
    path('login/', signin, name='login'),
]