from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum

from account.models import User
from .models import UserTimeTable, Course, ShibauraRule
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

        # 同じcourse_idが存在しなければ追加
        if not UserTimeTable.objects.filter(user_id=request.user, course_id=course_id).exists():
            usr_table = UserTimeTable(user_id=request.user, course_id=course_id, status='履修中')
            usr_table.save()

            # もし2コマの教科だったらその下の時限も登録
            # if course_id.subject_id.unit == 2:    

    # 履修登録ページにリダイレクト
    return redirect('tanni:reg')

@login_required
def reg_get(request,a,b,c,d,e,f,week,period):
    print(a,b,c,d,e,f,week,period)
    aa = bb = cc = dd = ee = ff = Course.objects.filter(subject_id__group='')
    if a == 1:
        aa = Course.objects.filter(subject_id__group='専門', week=week, period=period)
    if b == 1:
        bb = Course.objects.filter(subject_id__group='共通数理', week=week, period=period)
    if c == 1:
        cc = Course.objects.filter(subject_id__group='言語・情報系', week=week, period=period)
    if d == 1:
        dd = Course.objects.filter(subject_id__group='人文社会系教養', week=week, period=period)
    if e == 1:
        ee = Course.objects.filter(subject_id__group='共通健康', week=week, period=period)
    if f == 1:
        ff = Course.objects.filter(subject_id__group='共通工学系教養', week=week, period=period)
    
    course_list = aa.union(bb, cc, dd, ee, ff)
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
def sim_get(request,a,b,c,d,e,f):
    # セーブ処理
    obj = User.objects.get(id=request.user.id)
    obj.senmon = a
    obj.suuri = b
    obj.gengo = c
    obj.jinbun = d
    obj.kenkou = e
    obj.kougaku = f
    obj.save()

    # 集計
    us = UserTimeTable.objects.filter(user_id=request.user)
    re1 = us.filter(course_id__subject_id__group='専門').aggregate(Sum('course_id__subject_id__credit'))
    re2 = us.filter(course_id__subject_id__group='共通数理').aggregate(Sum('course_id__subject_id__credit'))
    re3 = us.filter(course_id__subject_id__group='言語・情報系').aggregate(Sum('course_id__subject_id__credit'))
    re4 = us.filter(course_id__subject_id__group='人文社会系教養').aggregate(Sum('course_id__subject_id__credit'))
    re5 = us.filter(course_id__subject_id__group='共通健康').aggregate(Sum('course_id__subject_id__credit'))
    re6 = us.filter(course_id__subject_id__group='共通工学系教養').aggregate(Sum('course_id__subject_id__credit'))
    r1 = re1['course_id__subject_id__credit__sum'] if re1['course_id__subject_id__credit__sum'] != None else 0
    r2 = re2['course_id__subject_id__credit__sum'] if re2['course_id__subject_id__credit__sum'] != None else 0
    r3 = re3['course_id__subject_id__credit__sum'] if re3['course_id__subject_id__credit__sum'] != None else 0
    r4 = re4['course_id__subject_id__credit__sum'] if re4['course_id__subject_id__credit__sum'] != None else 0
    r5 = re5['course_id__subject_id__credit__sum'] if re5['course_id__subject_id__credit__sum'] != None else 0
    r6 = re6['course_id__subject_id__credit__sum'] if re6['course_id__subject_id__credit__sum'] != None else 0
    summ = r1 + r2 + r3 + r4 + r5 + r6
    required = ShibauraRule.objects.filter(department='情報工学科').first().credit_for_graduation

    params = {
        'senmon':  str(r1 + a) + ' ('  + str(r1) + ')',
        'suuri':   str(r2 + b) + ' ('  + str(r2) + ')',
        'gengo':   str(r3 + c) + ' ('  + str(r3) + ')',
        'jinbun':  str(r4 + d) + ' ('  + str(r4) + ')',
        'kenkou':  str(r5 + e) + ' ('  + str(r5) + ')',
        'kougaku': str(r6 + f) + ' ('  + str(r6) + ')',
        'sum': summ,
        'required': required,
        'diff': required - summ,
    }
    return render(request, 'tanni/sim_tanni.html', params)


@login_required
def scraping(request):
    cnt = ccnt = 0
    url_list = [
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01131.html.ja', # 専門
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01161.html.ja', # 共通数理
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01162.html.ja', # 言語・情報系
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01163.html.ja', # 人文社会系教養
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01164.html.ja', # 共通健康
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01165.html.ja', # 共通工学系教養
        'http://syllabus.sic.shibaura-it.ac.jp/syllabus/2018/MatrixL01171.html.ja', # 全学共通科目群
    ]
    cnt += syllabus_scraping(url_list[0], "専門")
    cnt += syllabus_other_scraping(url_list[1], "共通数理")
    cnt += syllabus_other_scraping(url_list[2], "言語・情報系")
    cnt += syllabus_other_scraping(url_list[3], "人文社会系教養")
    cnt += syllabus_other_scraping(url_list[4], "共通健康")
    cnt += syllabus_other_scraping(url_list[5], "共通工学系教養")
    cnt += syllabus_other_scraping(url_list[6], "全学共通科目群")

    ccnt += time_scraping("http://timetable.sic.shibaura-it.ac.jp/table/2020/Timetable1L0113.html")

    params = {
        'url_list': url_list,
        'cnt': cnt,
        'ccnt': ccnt
    }
    return render(request, 'tanni/scraping.html', params)