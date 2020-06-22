from django.shortcuts import render
from account.models import User

def home(request):
    params = {
        
    }
    return render(request, 'tanni/home.html', params)

def userinfo(request):
    params = {
        
    }
    return render(request, 'tanni/userinfo.html', params)

def userlist(request):
    user_all = User.objects.all()
    params = {
        'user_all': user_all,
    }
    return render(request, 'tanni/userlist.html', params)

def reg(request):
    params = {
        
    }
    return render(request, 'tanni/reg.html', params)

def sim(request):
    params = {
        
    }
    return render(request, 'tanni/sim.html', params)