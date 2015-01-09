# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django_ajax.decorators import ajax

from core.models import ProductItem
from core.forms import ProductItemForm
from apps.alibabachina.scrap import ListingScrap
from apps.ebay.models import EbayStuff, EbayProductItem
from apps.ebay.forms import EbayProductItemForm
from apps.ebay.api import listing


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
    page = request.GET.get('page')
    items_list = ProductItem.objects.all().prefetch_related('ebayproductitem_set')

    paginator = Paginator(items_list, 25)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
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


def listing_detail_new(request):
    return render_to_response('listing-detail.html',
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
    result = 'failed'
    item_id = request.POST.get('id')
    if item_id:
        try:
            item = ProductItem.objects.get(id=item_id)
        except ProductItem.DoesNotExist:
            result = 'failed'
        else:
            form = ProductItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                result = 'succeed'
            else:
                print('ProductItemForm save failed.')
    return {'result': result}


def listing_detail_ebay(request, item_id):
    item = None
    if item_id:
        try:
            item = EbayProductItem.objects.get(id=item_id)
        except EbayProductItem.DoesNotExist:
            pass
        else:
            form = EbayProductItemForm(request.POST, instance=item)
    return render_to_response('listing-detail-ebay.html', {'item': item, 'form': form},
                              context_instance=RequestContext(request))


@ajax
def listing_detail_ebay_create(request):
    item_id = request.POST.get('id')
    ebay_item = None
    if item_id:
        # 保存
        item = ProductItem.objects.get(id=item_id)
        form = ProductItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        else:
            print('ProductItemForm save failed.')
        # 新建
        ebay_item = EbayProductItem(product_item=item)
        ebay_item.title = item.title
        ebay_item.describe = item.content
        ebay_item.images = item.images
        ebay_item.images_checked = item.images_checked
        ebay_item.save()
    return redirect('/listing/detail/ebay/%s/' % ebay_item.id)


@ajax
def listing_detail_ebay_save(request):
    result = 'failed'
    item_id = request.POST.get('id')
    if item_id:
        try:
            item = EbayProductItem.objects.get(id=item_id)
        except EbayProductItem.DoesNotExist:
            result = 'failed'
        else:
            form = EbayProductItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                result = 'succeed'
            else:
                print('EbayProductItemForm save failed.')
    return {'result': result}


@ajax
def listing_detail_ebay_list(request):
    result = 'failure'
    msg = ''
    url = ''
    item_id = request.POST.get('id')
    if item_id:
        try:
            item = EbayProductItem.objects.get(id=item_id)
        except EbayProductItem.DoesNotExist:
            return {'result': 'failure', 'msg': 'EbayProductItem.DoesNotExist'}
        else:
            form = EbayProductItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
        data = listing.add_fixed_price_item(listing.gen_data_by_item(item_id))
        # data = {"ItemID": "110154796762", "Errors": {"ErrorCode": "21916045", "LongMessage": "Shipping cost for additional items may not be greater than base shipping cost. Your Additional Shipping Cost has been reset to match the Shipping Cost value.", "ErrorClassification": "RequestError", "SeverityCode": "Warning", "ShortMessage": "Invalid AdditionalShippingCost."}, "Ack": "Warning", "Timestamp": "2015-01-09T04:56:03.929Z", "DiscountReason": "SpecialOffer", "Version": "899", "Build": "E899_UNI_API5_17299296_R1", "StartTime": "2015-01-09T04:56:03.492Z", "Fees": {"Fee": [{"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "AuctionLengthFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "BoldFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "BuyItNowFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "CategoryFeaturedFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "FeaturedFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "GalleryPlusFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "FeaturedGalleryFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "FixedPriceDurationFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "GalleryFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "GiftIconFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "HighLightFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "InsertionFee", "PromotionalDiscount": {"_currencyID": "USD", "value": "0.05"}}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "InternationalInsertionFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "ListingDesignerFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "ListingFee", "PromotionalDiscount": {"_currencyID": "USD", "value": "0.05"}}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "PhotoDisplayFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "PhotoFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "ReserveFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "SchedulingFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "SubtitleFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "BorderFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "ProPackBundleFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "BasicUpgradePackBundleFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "ValuePackBundleFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "PrivateListingFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "ProPackPlusBundleFee"}, {"Fee": {"_currencyID": "USD", "value": "0.0"}, "Name": "MotorsGermanySearchFee"}]}, "EndTime": "2015-02-08T04:56:03.492Z"}

        ack = data.get('Ack')
        if ack == 'Success':
            item_id = data.get('ItemID')
            start_time = data.get('StartTime')
            end_time = data.get('EndTime')
            item.item_id = item_id
            item.save()
            result = 'success'
            url = '物品：<a target="_blank" href="http://cgi.sandbox.ebay.com/ws/eBayISAPI.dll?ViewItem&item=%s">%s</a><br/>' % (item_id, item_id)
            pass
        elif ack == 'Warning':
            item_id = data.get('ItemID')
            start_time = data.get('StartTime')
            end_time = data.get('EndTime')
            error_code = data.get('Errors').get('ErrorCode')
            error_msg = data.get('Errors').get('LongMessage')
            item.item_id = item_id
            item.save()
            result = 'warning'
            msg = error_msg
            url = ' ebay物品: <a target="_blank" href="http://cgi.sandbox.ebay.com/ws/eBayISAPI.dll?ViewItem&item=%s">%s</a><br/>' % (item_id, item_id)
            pass
        elif ack == 'Failure':
            error_code = data.get('Errors').get('ErrorCode')
            error_msg = data.get('Errors').get('LongMessage')
            msg = error_msg
            pass
    return {'result': result, 'msg': msg, 'url': url}