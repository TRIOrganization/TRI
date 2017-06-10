# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_img', models.ImageField(upload_to=b'')),
                ('caption_heder', models.CharField(max_length=200)),
                ('caption_letter', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AndroidApplicationProgramming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='ArtificialIntellignece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_img', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='DesktopApplicationProgramming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='InformationSecurity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Networking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_img', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkProgramming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to=b'')),
                ('slider_caption', models.CharField(max_length=200)),
                ('slider_header', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='WebDeveloping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('letter', models.CharField(max_length=400)),
            ],
        ),
    ]