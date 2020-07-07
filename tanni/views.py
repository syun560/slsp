from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    total_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_graduation # 卒業要件
    reserch_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_research # 卒研着手
    special_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_graduation # 専門
    math_sci_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_graduation # 共通数理
    lang_info_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_graduation # 言語情報系
    jinbun_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_graduation # 人文社会科目
    health_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_graduation # 共通健康
    tech_grad = ShibauraRule.objects.filter(department="情報工学科", year=2018).first().credit_for_graduation # 共通工学

    params = {
        'total_grad': total_grad,
        'reserch_grad': reserch_grad,
        'special_grad': special_grad,
        'math_sci_grad': math_sci_grad,
        'lang_sci_grad': lang_info_grad,
        'jinbun_grad': jinbun_grad,
        'health_grad': health_grad,
        'tech_grad': tech_grad,
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