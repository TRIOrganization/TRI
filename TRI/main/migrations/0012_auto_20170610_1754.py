# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170610_1649'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DesktopApplicationProgramming',
            new_name='Programming',
        ),
        migrations.DeleteModel(
            name='AndroidApplicationProgramming',
        ),
        migrations.DeleteModel(
            name='NetworkProgramming',
        ),
    ]
