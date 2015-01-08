# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django_ajax.decorators import ajax

from apps.ebay.api import category


@ajax
def gen_category(request):
    # utils.fetch_categories()
    # utils.gen_categories()
    category.get_categories()
    return {'result': 'succeed'}