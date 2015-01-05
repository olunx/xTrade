# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django import template

register = template.Library()


@register.inclusion_tag('listing-detail-ebay.html')
def listing_detail_ebay(item):
    return {'item': item}