from django.urls import path
from . import views

app_name = 'tanni'

urlpatterns = [
    path('', views.home, name='home'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('userlist/', views.userlist, name='userlist'),
    path('reg/', views.reg, name='reg'),
    path('sim/', views.sim, name='sim'),
]