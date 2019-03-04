from django.db import models


class Movie(models.Model):
    name = models.CharField(verbose_name="电影名称",max_length=30)
    year = models.CharField(verbose_name="发行年份")
    director = models.CharField(verbose_name="导演",max_length=10)
    actor = models.CharField()
