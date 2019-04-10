# Generated by Django 2.1.7 on 2019-03-14 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='博客名称')),
                ('content', models.TextField(verbose_name='博客正文')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
            },
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='标签名')),
                ('add_time', models.DateField(auto_now_add=True)),
                ('desc', models.CharField(max_length=200, verbose_name='标签描述')),
            ],
            options={
                'verbose_name': '博客标签',
                'verbose_name_plural': '博客标签',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='Tag',
            field=models.ManyToManyField(to='blog.BlogTag', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
