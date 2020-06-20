from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('userlist/', views.userlist, name='userlist'),
]