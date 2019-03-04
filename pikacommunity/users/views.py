from django.shortcuts import render
from django.views.generic.base import View
from .forms import RegisterForm
from captcha.fields import CaptchaStore
from captcha.views import captcha_image_url
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from utils.user_util import send_message


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
            if UserProfile.objects.filter(email=email):
                return render(request,'register',{'msg':'该邮箱已被注册'})
            username = request.POST.get("email","")
            password = request.POST.get("password","")
            user = UserProfile()
            user.username = username
            user.password = make_password(password)
            user.is_active = False
            user.save()

            send_status = send_message(email,email_type='register')
            if send_status:
                return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form,'msg':'请验证您的邮箱或者验证码'})