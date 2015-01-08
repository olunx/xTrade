# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.forms import ModelForm

from apps.ebay.models import EbayProductItem


class EbayProductItemForm(ModelForm):
    class Meta:
        model = EbayProductItem
        fields = ['account', 'site_id', 'list_type',
                  'ebay_cat_primary', 'ebay_cat_secondary', 'store_cat_primary', 'store_cat_secondary',
                  'title', 'describe', 'images', 'images_checked',
                  'price', 'quality', 'duration', 'item_location', 'item_country',
                  'item_postal', 'dispatch_time_max', 'shipping_internal_service', 'shipping_internal_cost',
                  'shipping_internal_additional_cost', 'shipping_international_service', 'shipping_international_cost',
                  'shipping_international_additional_cost', 'shipping_international_area', 'payment_account']