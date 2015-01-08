# -*- coding: utf-8 -*-
__author__ = 'olunx'

import ast
import time
import datetime

from django_ajax.decorators import ajax
import goslate


@ajax
def translate(request):
    text = request.POST.get('text')
    lang = request.POST.get('lang')
    if text and lang:
        gs = goslate.Goslate()
        return {'result': gs.translate(text, lang)}


def get_time_stamp():
    return '%s%s' % (datetime.datetime.now().strftime('%Y%m%d%H%M%s'), time.clock())


def get_image_list(images):
    data = []
    if images:
        data = ast.literal_eval(images)
    return list(set(data))