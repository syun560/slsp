from django.shortcuts import render

# Create your views here.

def home(request):
    params = {
        
    }
    return render(request, 'tanni/home.html', params)

def userinfo(request):
    params = {
        
    }
    return render(request, 'tanni/userinfo.html', params)

def userlist(request):
    params = {
        
    }
    return render(request, 'tanni/userlist.html', params)