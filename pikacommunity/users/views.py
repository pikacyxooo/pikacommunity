from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm,LoginForm
from .models import UserProfile,EmailVerifyRecord
from captcha.fields import CaptchaStore
from captcha.views import captcha_image_url
from utils.user_util import send_message
from utils.mixin_utils import LoginRequiredMixin


class CustomBackend(ModelBackend):
    """验证用户登录的ModelBackend"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    """用户注册的视图函数"""
    def get(self,request):
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        register_form = RegisterForm()
        return render(request,'register.html',locals())

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email","")
            if UserProfile.objects.filter(username=email):
                return render(request,'register.html',{'register_form':register_form,'msg':'该邮箱已被注册'})
            username = request.POST.get("email","")
            password = request.POST.get("password","")
            user = UserProfile()
            user.username = username
            user.email = email
            user.password = make_password(password)
            user.is_active = False
            user.save()

            send_status = send_message(email,email_type='register')
            if send_status:
                return render(request,'register_after.html')
        else:
            return render(request,'register.html',{'register_form':register_form,'msg':'请验证您的邮箱或者验证码'})


class ActiveUserView(View):
    def get(self,request,active_code):
        records = EmailVerifyRecord.objects.filter(code=active_code)
        if records:
            for record in records:
                user = UserProfile.objects.get(username=record.email)
                user.is_active = True
                user.save()
                return render(request,'login.html')
        else:
            return render(request,'active_fail.html')


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            user = authenticate(username=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
                else:
                    return render(request,'login.html',{'msg':'该用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        return render(request, 'login.html', {'msg': '用户名或密码错误'})


class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

