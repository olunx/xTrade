# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django_ajax.decorators import ajax

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
    items = ProductItem.objects.all().prefetch_related('ebayproductitem_set')
    return render_to_response('listing-list.html', {'items': items},
                              context_instance=RequestContext(request))


def listing_detail(request, item_id):
    item = None
    if item_id:
        try:
            item = ProductItem.objects.get(id=item_id)
        except ProductItem.DoesNotExist:
            pass

    return render_to_response('listing-detail.html', {'item': item},
                              context_instance=RequestContext(request))


@ajax
def listing_detail_create(request):
    page = request.POST.get('page')
    item_id = None
    if page:
        scrap = ListingScrap()
        item_id = scrap.scrap_page(page)
    return redirect('/listing/detail/%s/' % item_id)


@ajax
def listing_detail_save(request):
    item_id = request.POST.get('id')
    result = 'failed'
    if item_id:
        try:
            item = ProductItem.objects.get(id=item_id)
        except ProductItem.DoesNotExist:
            result = 'failed'
        else:
            item.title = request.POST.get('title')
            item.purchasing_price = request.POST.get('purchasing_price')
            item.purchasing_location = request.POST.get('purchasing_location')
            item.purchasing_shipping = request.POST.get('purchasing_shipping')
            item.save()
            result = 'succeed'
    return {'result': result}


def listing_detail_ebay(request, item_id):
    item = None
    if item_id:
        try:
            item = EbayProductItem.objects.get(id=item_id)
        except EbayProductItem.DoesNotExist:
            pass
    return render_to_response('listing-detail-ebay.html', {'item': item},
                              context_instance=RequestContext(request))


@ajax
def listing_detail_ebay_create(request):
    item_id = request.POST.get('id')
    ebay_item = None
    if item_id:
        # 保存
        item = ProductItem.objects.get(id=item_id)
        item.title = request.POST.get('title')
        item.purchasing_price = request.POST.get('purchasing_price')
        item.purchasing_location = request.POST.get('purchasing_location')
        item.purchasing_shipping = request.POST.get('purchasing_shipping')
        item.save()
        # 新建
        ebay_item = EbayProductItem(product_item=item)
        ebay_item.title = item.title
        ebay_item.describe = item.content
        ebay_item.images = item.images
        ebay_item.save()

    return redirect('/listing/detail/ebay/%s/' % ebay_item.id)