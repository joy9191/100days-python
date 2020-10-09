# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-25 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMsg',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6587\u7ae0\u521b\u5efa\u65f6\u95f4')),
                ('author', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u7f16\u8f91\u59d3\u540d')),
                ('createtime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]