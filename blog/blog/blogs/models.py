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
    createtime = models.DateTimeField(auto_now_add=True)