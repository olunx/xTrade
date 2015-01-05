# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django_ajax.decorators import ajax
import goslate


@ajax
def translate(request):
    text = request.POST.get('text')
    lang = request.POST.get('lang')
    if text and lang:
        gs = goslate.Goslate()
        return {'result': gs.translate(text, lang)}