# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django import template

from apps.ebay.api import category


register = template.Library()


@register.inclusion_tag('categories_select_ebay.html')
def categories_select_ebay():
    items = category.get_categories()
    print 'items %s' % items
    return {'items': items}