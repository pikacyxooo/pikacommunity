from django.db import models
from users.models import UserProfile
from ckeditor.fields import RichTextField


class BlogTag(models.Model):
    name = models.CharField(max_length=30,verbose_name='标签名')
    add_time = models.DateField(auto_now_add=True)
    desc = models.CharField(max_length=200,verbose_name='标签描述')
    click_num = models.IntegerField(default=0,verbose_name="点击数")

    class Meta:
        verbose_name = "博客标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100,verbose_name="博客名称")
    author = models.ForeignKey(UserProfile,on_delete=models.DO_NOTHING,verbose_name="作者")
    tag = models.ManyToManyField(BlogTag,verbose_name="类型")
    content = RichTextField()
    create_time = models.DateTimeField(auto_now_add=True)
    click_num = models.IntegerField(default=0,verbose_name="博客点击数")

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name


    def get_tag(self):
        return self.tag.all()


    def __str__(self):
        return "{}    Blog:{}".format(self.author,self.name)