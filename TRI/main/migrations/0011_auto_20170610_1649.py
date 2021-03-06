# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170610_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aim',
            name='caption_letter',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='androidapplicationprogramming',
            name='letter',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='desktopapplicationprogramming',
            name='letter',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='informationsecurity',
            name='letter',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='networking',
            name='letter',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='networkprogramming',
            name='letter',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_header',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='webdeveloping',
            name='letter',
            field=models.TextField(max_length=800),
        ),
    ]
