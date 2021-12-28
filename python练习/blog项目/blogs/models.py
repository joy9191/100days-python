# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class BlogMsg(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='标题')
    # content = models.CharField(max_length=512,verbose_name='正文')
    content = models.TextField(verbose_name='正文')
    date = models.CharField(max_length=50, verbose_name='文章创建时间', blank=True, null=True)
    # date = models.DateTimeField(verbose_name='文章创建时间', default = timezone.now)
    author = models.CharField(max_length=30, blank=True, null=True, verbose_name='编辑姓名')
    createtime = models.DateTimeField(auto_now=True)


class User(models.Model):
    """用户"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    tel = models.CharField(max_length=20, verbose_name='手机号')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    last_visit = models.DateTimeField(null=True, verbose_name='最后登录时间')

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'
