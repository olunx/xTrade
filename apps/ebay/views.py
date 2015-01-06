# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext

from django_ajax.decorators import ajax

from apps.ebay import utils


@ajax
def gen_category(request):
    # utils.fetch_categories()
    # utils.gen_categories()
    utils.get_categories()
    return {'result': 'succeed'}