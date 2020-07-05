from django.db import models
from account.models import User

# C7.M1 科目情報モデル
class Subject(models.Model):
    title = models.CharField(verbose_name='科目名', max_length=64)
    group = models.CharField(verbose_name='分類', max_length=64)
    credit = models.IntegerField(verbose_name='単位数')
    unit = models.IntegerField(verbose_name='コマ数')
    required = models.CharField(verbose_name='必修', default=1, max_length=64)

    def __str__(self):
        return self.title

# C7.M2 開講科目情報モデル
class Course(models.Model):
    subject_id = models.ForeignKey(Subject, verbose_name='科目id', on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='年度')
    term = models.IntegerField(verbose_name='期')
    week = models.IntegerField(verbose_name='曜日')
    period = models.IntegerField(verbose_name='時限')
    place = models.CharField(verbose_name='開講場所', max_length=64)
    teacher = models.CharField(verbose_name='教員氏名', max_length=64)

    def __str__(self):
        return str(self.subject_id) + str(self.week) + str(self.period)


# C7.M3 学則情報モデル
class ShibauraRule(models.Model):
    department = models.CharField(verbose_name='学科', max_length=64)
    year = models.IntegerField(verbose_name='入学年度')
    credit_for_graduation = models.IntegerField(verbose_name='卒業必須単位')
    credit_for_research = models.IntegerField(verbose_name='卒検着手必須単位')

    def __str__(self):
        return self.department

# C6.M2 ユーザ時間割モデル（本来ここに書くべきでない、あとで移動するかも）
class UserTimeTable(models.Model):
    user_id = models.ForeignKey(User, verbose_name='ユーザid', on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, verbose_name='開講科目id', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='履修状況', max_length=64)
    def __str__(self):
        return str(self.user_id)
