# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-17 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='desc',
            field=models.TextField(default='', verbose_name='对权限的描述'),
            preserve_default=False,
        ),
    ]