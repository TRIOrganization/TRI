# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 18:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20170611_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='networking',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 10, 18, 34, 40, 391250, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
