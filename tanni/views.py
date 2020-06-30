from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.models import User
from .models import UserTimeTable, Course

def getTimeTable(id):
    # ログインユーザの履修している科目を取得
    user_table = UserTimeTable.objects.filter(user_id=id)

    # 時間割に適した形で取得
    time_table = [["" for s in range(6)] for ss in range(5)]
    for tt in user_table:
        time_table[tt.course_id.period - 1][tt.course_id.week - 1] = tt.course_id.subject_id.title

    return time_table

@login_required
def home(request):
    params = {
        'time_table': getTimeTable(request.user),
    }
    return render(request, 'tanni/home.html', params)

@login_required
def userinfo(request, student_id):
    # 学籍番号からUserを取得
    selected_user = User.objects.filter(student_id=student_id).first()
    params = {
        'time_table': getTimeTable(selected_user.id),
        'selected_user': selected_user,
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
        'time_table': getTimeTable(request.user),
    }
    return render(request, 'tanni/reg.html', params)

@login_required
def sim(request):
    params = {
        
    }
    return render(request, 'tanni/sim.html', params)