# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170611_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
