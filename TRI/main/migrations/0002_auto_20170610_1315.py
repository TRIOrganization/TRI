# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aim',
            name='background_img',
        ),
        migrations.RemoveField(
            model_name='androidapplicationprogramming',
            name='slider_img',
        ),
        migrations.RemoveField(
            model_name='artificialintellignece',
            name='background_img',
        ),
        migrations.RemoveField(
            model_name='desktopapplicationprogramming',
            name='slider_img',
        ),
        migrations.RemoveField(
            model_name='informationsecurity',
            name='slider_img',
        ),
        migrations.RemoveField(
            model_name='networking',
            name='background_img',
        ),
        migrations.RemoveField(
            model_name='networkprogramming',
            name='slider_img',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider_img',
        ),
        migrations.RemoveField(
            model_name='webdeveloping',
            name='slider_img',
        ),
    ]