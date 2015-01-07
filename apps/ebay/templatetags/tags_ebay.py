# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django import template
from apps.ebay import utils

register = template.Library()


@register.inclusion_tag('categories_select_ebay.html')
def categories_select_ebay():
    items = utils.get_categories()
    print 'items %s' % items
    return {'items': items}