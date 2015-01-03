# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import apps.alibabachina.views as alibabachina
from apps.alibabachina.models import AlibabachinaScrapy
from apps.ebay.models import EbayStuff


def home(request):
    return render_to_response('index.html')


def hot_stuff(request):
    category = request.GET.get('category')
    page = request.GET.get('page')

    if category and category != 'None':
        stuffs_list = EbayStuff.objects.filter(category__contains=category).order_by('-sold')
    else:
        category = 0
        stuffs_list = EbayStuff.objects.all().order_by('-sold')

    paginator = Paginator(stuffs_list, 25)
    try:
        stuffs = paginator.page(page)
    except PageNotAnInteger:
        stuffs = paginator.page(1)
    except EmptyPage:
        stuffs = paginator.page(paginator.num_pages)

    return render_to_response('hot-stuff.html', {'category': category, 'stuffs': stuffs},
                              context_instance=RequestContext(request))


def scrap_page(request):
    page = request.GET.get('page')
    if not page:
        page = request.POST.get('page')
    if page:
        # alibabachina.scrap_page(page)
        try:
            item = AlibabachinaScrapy.objects.get(url=page)
        except AlibabachinaScrapy.DoesNotExist:
            pass
    else:
        item = None
    return render_to_response('scrapy.html', {'item': item},
                              context_instance=RequestContext(request))


def listing_list(request):
    items = AlibabachinaScrapy.objects.all()
    return render_to_response('listing-list.html', {'items': items},
                              context_instance=RequestContext(request))