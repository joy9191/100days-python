# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-11 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200925_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmsg',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
