# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-09 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_article_must_show'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name_plural': 'Campusses'},
        ),
        migrations.AddField(
            model_name='campus',
            name='campus_image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
