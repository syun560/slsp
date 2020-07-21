from django.urls import path
from . import views

app_name = 'tanni'

urlpatterns = [
    path('', views.home, name='home'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('user/', views.userlist, name='userlist'),
    path('user/<student_id>', views.userinfo, name='userlist'),
    
    path('reg/', views.reg, name='reg'),
    path('reg_add/', views.reg_add, name='reg_add'),
    path('reg_get/<int:a>,<int:b>,<int:c>,<int:d>,<int:e>,<int:f>/<int:week>/<int:period>/', views.reg_get, name='reg_get'),
    path('reg_delete/', views.reg_delete, name='reg_delete'),

    path('sim/', views.sim, name='sim'),
    path('sim_get/<int:a>,<int:b>,<int:c>,<int:d>,<int:e>,<int:f>/', views.sim_get, name='sim_get'),
    
    path('scraping/', views.scraping, name='scraping'),
]