from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm

# Create your views here.
class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

class Logout(LogoutView):
    template_name = 'account/logout.html'