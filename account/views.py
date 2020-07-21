from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm

# Create your views here.
class Login(LoginView):
    """ C1.M1: ログイン処理を行う
    """
    form_class = LoginForm
    template_name = 'account/login.html'

class Logout(LogoutView):
    """ C1.M2: ログアウト処理を行う
    """
    template_name = 'account/logout.html'
