# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django import forms

from apps.ebay.models import EbayProductItem

SITE_ID_CHOICES = (
    ('0', u'美国'),
    ('1', u'加拿大(英语)'),
    ('25', u'加拿大(法语)'),
    ('2', u'英国'),
    ('3', u'澳大利亚'),
    ('4', u'奥地利'),
    ('5', u'比利时(法语)'),
    ('9', u'比利时(荷兰语)'),
    ('6', u'法国'),
    ('7', u'德国'),
    ('8', u'意大利'),
    ('10', u'荷兰'),
    ('11', u'西班牙'),
    ('12', u'瑞士'),
    ('14', u'eBay 汽车'),
    ('15', u'香港'),
    ('16', u'新加坡'),
    ('17', u'印度'),
    ('19', u'爱尔兰'),
    ('20', u'马来西亚'),
    ('21', u'菲律宾'),
    ('22', u'波兰'),
)

LIST_TYPE_CHOICES = (
    ('Chinese', u'拍卖'),
    ('FixedPriceItem', u'固价'),
    ('3', u'多属性'),
)

DURATION_CHOICES = (
    ('Days_3', '3 days'),
    ('Days_5', '5 days'),
    ('Days_7', '7 days'),
    ('Days_10', '10 days'),
    ('Days_30', '30 days'),
    ('GTC', 'GTC'),
)

COUNTRY_CHOICES = (
    ('CN', u'中国'),
    ('US', u'美国'),
)

DISPATCH_TIME_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class EbayProductItemForm(forms.ModelForm):
    site_id = forms.ChoiceField(choices=SITE_ID_CHOICES, widget=forms.Select())
    list_type = forms.ChoiceField(choices=LIST_TYPE_CHOICES, widget=forms.RadioSelect())
    duration = forms.ChoiceField(choices=DURATION_CHOICES, widget=forms.Select())
    item_country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select())
    dispatch_time_max = forms.ChoiceField(choices=DISPATCH_TIME_CHOICES, widget=forms.Select())

    class Meta:
        model = EbayProductItem
        fields = ['account', 'site_id', 'list_type',
                  'ebay_cat_primary', 'ebay_cat_secondary', 'store_cat_primary', 'store_cat_secondary',
                  'title', 'describe', 'images', 'images_checked',
                  'price', 'quality', 'duration', 'item_location', 'item_country',
                  'item_postal', 'dispatch_time_max', 'shipping_internal_service', 'shipping_internal_cost',
                  'shipping_internal_additional_cost', 'shipping_international_service', 'shipping_international_cost',
                  'shipping_international_additional_cost', 'shipping_international_area',
                  'payment_method', 'payment_account']

