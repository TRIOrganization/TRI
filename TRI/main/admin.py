# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class SliderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Slider Information', {'fields':['slider_caption','slider_text']}),
        ('Slider Image', {'fields':['slider_image'], 'classes':['collapse']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    list_display = ('slider_caption', 'pub_date', 'slider_image', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ('slider_caption',)


class WebDevelopingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description About Our Project', {'fields':['caption', 'letter']}),
        ('Project Slider Image', {'fields': ['slide_image_1','slide_image_2','slide_image_3']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    list_display = ('caption', 'pub_date', 'was_published_recently')


class InformationSecurityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description About Our Project', {'fields':['caption', 'letter']}),
        ('Project Slider Image', {'fields': ['slide_image_1','slide_image_2','slide_image_3']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    list_display = ('caption', 'pub_date', 'was_published_recently')


class NetworkingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description About Our Project', {'fields':['caption', 'letter']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    list_display = ('caption', 'pub_date', 'was_published_recently')


class ArtificialIntelligneceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description About Our Project', {'fields':['caption', 'letter']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    list_display = ('caption', 'pub_date', 'was_published_recently')


class ProgrammingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description About Our Project', {'fields':['caption', 'letter']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    list_display = ('caption', 'pub_date', 'was_published_recently')


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Member Information', {'fields': ['name','position','biography']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    list_display = ('name','position', 'pub_date', 'was_published_recently')


class AimAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tri Organization Aim', {'fields':['caption_header', 'caption_letter']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    list_display = ('caption_header', 'pub_date', 'was_published_recently')


admin.site.register(Slider, SliderAdmin)
admin.site.register(WebDeveloping, WebDevelopingAdmin)
admin.site.register(InformationSecurity, InformationSecurityAdmin)
admin.site.register(Networking, NetworkingAdmin)
admin.site.register(ArtificialIntellignece, ArtificialIntelligneceAdmin)
admin.site.register(Aim, AimAdmin)
admin.site.register(Programming, ProgrammingAdmin)
admin.site.register(Member, MemberAdmin)
