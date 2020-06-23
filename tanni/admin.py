from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(ShibauraRule)
admin.site.register(UserTimeTable)
