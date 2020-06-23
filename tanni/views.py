from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.models import User
from .models import UserTimeTable

@login_required
def home(request):

    # ログインユーザの履修している科目を取得
    time_table = UserTimeTable.objects.filter(user_id=request.user)
    params = {
        'time_table': time_table,
    }
    return render(request, 'tanni/home.html', params)

@login_required
def userinfo(request):
    params = {
        
    }
    return render(request, 'tanni/userinfo.html', params)

@login_required
def userlist(request):

    # すべてのユーザの情報を取得
    user_all = User.objects.all()
    params = {
        'user_all': user_all,
    }
    return render(request, 'tanni/userlist.html', params)

@login_required
def reg(request):
    params = {
        
    }
    return render(request, 'tanni/reg.html', params)

@login_required
def sim(request):
    params = {
        
    }
    return render(request, 'tanni/sim.html', params)