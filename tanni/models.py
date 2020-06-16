from django.db import models

# C6.M1 科目情報モデル
class Subject(models.Model):
    title = models.Charfield(verbose_name='科目名', max_length=64)
    group = models.Charfield(verbose_name='分類', max_length=64)
    credit = models.Integerfield(verbose_name='単位数')
    required = models.Charfield(verbose_name='必修', max_length=64)

    def __str__(self):
        return self.title

# C6.M2 開講科目情報モデル
class Course(models.Model):
    subject_id = models.ForeignKey(Subject, verbose_name='科目id', on_delete=models.CASCADE)
    year = models.Integerfield(verbose_name='年度')
    term = models.Integerfield(verbose_name='期')
    week = models.Integerfield(verbose_name='曜日')
    period = models.Integerfield(verbose_name='時限')
    place = models.Charfield(verbose_name='開講場所', max_length=64)
    teacher = models.Charfield(verbose_name='教員氏名', max_length=64)

    def __str__(self):
        return self.subject_id + self.week + self.period

# C6.M3 学則情報モデル
class ShibauraRule(models.Model):
    department = models.Charfield(verbose_name='学科', max_length=64)
    year = models.Integerfield(verbose_name='入学年度')
    credit_for_graduation = models.Integerfield(verbose_name='卒業必須単位')
    credit_for_research = models.Integerfield(verbose_name='卒検着手必須単位')

    def __str__(self):
        return self.department
