# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models



class Slider(models.Model):
    slider_img = models.FileField(null=True, blank=True)
    slider_caption = models.CharField(max_length=200)
    slider_header = models.TextField(max_length=300)

    def __str__(self):
        return self.slider_caption


class Aim(models.Model):
    caption_header = models.CharField(max_length=200)
    caption_letter = models.TextField(max_length=800)

    def __str__(self):
        return self.caption_header


class InformationSecurity(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)

    def __str__(self):
        return self.caption


class WebDeveloping(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)

    def __str__(self):
        return self.caption


class Networking(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)

    def __str__(self):
        return self.caption


class Programming(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)

    def __str__(self):
        return self.caption



class ArtificialIntellignece(models.Model):
    caption = models.CharField(max_length=200)
    letter = models.TextField(max_length=800)

    def __str__(self):
        return self.caption
