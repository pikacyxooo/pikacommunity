from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nickname = models.CharField(verbose_name="用户昵称",max_length=30,blank=True,null=True)
    mobile = models.CharField(verbose_name="用户电话",max_length=11,blank=True,null=True)
    image = models.ImageField(upload_to="image/%Y/%m",default='img/default.png',max_length=100)
    gender = models.CharField(choices=(('male','男'),('female','女')),max_length=6,default='female')
    address = models.CharField(max_length=100,default='北京市')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(verbose_name='验证码类型',choices=(('register','注册'),('forget','忘记密码')),max_length=20)
    send_time = models.DateField(auto_now_add=True,verbose_name='验证码发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}->{}'.format(self.email,self.code)
