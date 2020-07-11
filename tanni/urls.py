from django.urls import path
from . import views

app_name = 'tanni'

urlpatterns = [
    path('', views.home, name='home'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('user/', views.userlist, name='userlist'),
    path('user/<student_id>', views.userinfo, name='userlist'),
    
    path('reg/', views.reg, name='reg'),
    path('reg_delete/', views.reg_delete, name='reg_delete'),

    path('sim/', views.sim, name='sim'),
    
    path('scraping/', views.scraping, name='scraping'),
]