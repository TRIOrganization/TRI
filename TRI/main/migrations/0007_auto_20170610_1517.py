# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170610_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artificialintellignece',
            name='letter',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_img',
            field=models.ImageField(default=None, upload_to='./static/main/img/'),
        ),
    ]
