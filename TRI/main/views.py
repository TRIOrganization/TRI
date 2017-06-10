# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    ai = get_object_or_404(ArtificialIntellignece, pk=1)
    slider = Slider.objects.all()
    aim = Aim.objects.all()
    i_s = InformationSecurity.objects.all()
    wd = WebDeveloping.objects.all()
    nw = Networking.objects.all()
    pm = Programming.objects.all()
    
    context = {
        'ai_header': ai.caption,
        'ai_letter': ai.letter,
        'slider': slider,
        'aim': aim,
        'i_s': i_s,
        'wd': wd,
        'nw': nw,
        'pm': pm,
        }
    return render(request, 'main/index.html', context)
