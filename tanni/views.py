from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.models import User
from .models import UserTimeTable, Course

@login_required
def home(request):
    # ログインユーザの履修している科目を取得
    time_table = UserTimeTable.objects.filter(user_id=request.user)

    # 時間割に適した形で取得
    jikanwari = [["" for s in range(6)] for ss in range(5)]
    for tt in time_table:
        jikanwari[tt.course_id.period - 1][tt.course_id.week - 1] = tt.course_id.subject_id.title

    params = {
        'jikanwari': jikanwari,
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