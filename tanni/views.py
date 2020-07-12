from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from account.models import User
from .models import UserTimeTable, Course
from .scraping import *

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
    # 共通処理、すべてのユーザの情報を取得
    user_list = User.objects.all()

    # POSTアクセス時の処理、絞り込み
    if request.method == 'POST':
        search_word = request.POST['faculty'] + request.POST['department']
        user_list = User.objects.filter(student_id__contains=search_word)

    params = {
        'user_list': user_list,
    }
    return render(request, 'tanni/userlist.html', params)

@login_required
def reg(request):
    params = {
        'time_table': getTimeTable(request.user),
    }
    return render(request, 'tanni/reg.html', params)

@login_required
def reg_add(request):
    if request.method=='POST':
        # 時間割追加処理
        course_id = Course.objects.filter(subject_id__title=request.POST['subject']).first()

        # 追加
        usr_table = UserTimeTable(user_id=request.user, course_id=course_id, status='履修中')
        usr_table.save()

    # 履修登録ページにリダイレクト
    return redirect('tanni:reg')

@login_required
def reg_get(request,a,b,c,d,e,f):
    print(a,b,c,d,e,f)
    # course_list = Course.objects.filter(subject_id__group='専門')
    course_list = Course.objects.all()
    params = {
        'course_list': course_list,
    }
    return render(request, 'tanni/myDIV4.html', params)

@login_required
def reg_delete(request):
    # 時間割削除処理
    week = request.POST['week']
    period = request.POST['period']

    # 削除
    usr_table = UserTimeTable.objects.filter(course_id__week=week, course_id__period=period).first()
    usr_table.delete()

    # 履修登録ページにリダイレクト
    return redirect('tanni:reg')

@login_required
def sim(request):
    params = {
        
    }
    return render(request, 'tanni/sim.html', params)


@login_required
def scraping(request):
    # time_scraping()

    cnt = ccnt = 0
    url_list = [
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01131.html.ja', # 専門
        # 'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01161.html.ja', # 共通数理
        # 'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01162.html.ja', # 言語・情報系
        # 'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01163.html.ja', # 人文社会系教養
        # 'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01164.html.ja', # 共通健康
        # 'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01165.html.ja', # 共通工学系教養
        # 'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01171.html.ja', # 全学共通科目群
    ]
    cnt += syllabus_scraping(url_list[0], "専門")
    # cnt += syllabus_scraping(url_list[1], "共通数理")
    # cnt += syllabus_scraping(url_list[2], "言語・情報系")
    # cnt += syllabus_scraping(url_list[3], "人文社会系教養")
    # cnt += syllabus_scraping(url_list[4], "共通健康")
    # cnt += syllabus_scraping(url_list[5], "共通工学系教養")
    # cnt += syllabus_scraping(url_list[6], "全学共通科目群")

    ccnt += time_scraping("http://timetable.sic.shibaura-it.ac.jp/table/2020/Timetable1L0113.html")

    params = {
        'url_list': url_list,
        'cnt': cnt,
        'ccnt': ccnt
    }
    return render(request, 'tanni/scraping.html', params)