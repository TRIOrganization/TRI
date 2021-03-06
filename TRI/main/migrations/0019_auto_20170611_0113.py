# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 18:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_artificialintellignece_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 10, 18, 43, 37, 653150, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programming',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 10, 18, 43, 43, 737110, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
