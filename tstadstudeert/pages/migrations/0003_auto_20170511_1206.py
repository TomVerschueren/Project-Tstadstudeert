# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20170511_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_campus_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_school_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_study_name',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]