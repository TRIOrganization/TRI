# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime


class Slider(models.Model):
    slider_image = models.FileField(null=True, blank=True)
    slider_caption = models.CharField(max_length=200)
    slider_text = models.TextField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.slider_caption

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Aim(models.Model):
    caption_header = models.CharField(max_length=200)
    caption_letter = models.TextField(max_length=800)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.caption_header

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class InformationSecurity(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)
    pub_date = models.DateTimeField('date published')
    slide_image_1 = models.FileField(null=True, blank=True)
    slide_image_2 = models.FileField(null=True, blank=True)
    slide_image_3 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.caption

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class WebDeveloping(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)
    pub_date = models.DateTimeField('date published')
    slide_image_1 = models.FileField(null=True, blank=True)
    slide_image_2 = models.FileField(null=True, blank=True)
    slide_image_3 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.caption

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Networking(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.caption

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Programming(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)
    pub_date = models.DateTimeField('date published')
    slide_image_1 = models.FileField(null=True, blank=True)
    slide_image_2 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.caption

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class ArtificialIntellignece(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.caption

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Member(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    biography = models.TextField(max_length=800)
    pub_date = models.DateTimeField('date published')
    profile_image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
