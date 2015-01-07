# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import ProductItem
from apps.alibabachina.listing import ListingScrap
from apps.ebay.models import EbayStuff, EbayProductItem


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


def listing_list(request):
    items = ProductItem.objects.all()
    return render_to_response('listing-list.html', {'items': items},
                              context_instance=RequestContext(request))


def listing_detail(request):
    item_id = request.GET.get('id')
    page = request.POST.get('page')
    item = None
    if item_id:
        try:
            item = ProductItem.objects.get(id=item_id)
        except ProductItem.DoesNotExist:
            pass
    if page:
        scrap = ListingScrap()
        item_id = scrap.scrap_page(page)
        try:
            item = ProductItem.objects.get(id=item_id)
        except ProductItem.DoesNotExist:
            pass
    return render_to_response('listing-detail.html', {'item': item},
                              context_instance=RequestContext(request))


def listing_detail_ebay(request):
    item_id = request.GET.get('id')
    item = None
    if id:
        try:
            item = EbayProductItem.objects.get(id=item_id)
        except EbayProductItem.DoesNotExist:
            pass
    return render_to_response('listing-detail-ebay.html', {'item': item},
                              context_instance=RequestContext(request))