# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.db import models

from core.models import ProductItem
import core.utils as utils


# 爬虫数据对象

class EbayStuff(models.Model):
    item_id = models.CharField(max_length=30, unique=True, verbose_name='Ebay ID')
    url = models.CharField(max_length=256, null=True, verbose_name='URL')
    title = models.CharField(max_length=100, null=True, verbose_name='Title')
    subtitle = models.CharField(max_length=100, null=True, verbose_name='Subtitle')
    sold = models.IntegerField(null=True, verbose_name='Sold')
    watching = models.IntegerField(null=True, verbose_name='Watching')
    country = models.CharField(max_length=30, null=True, verbose_name='Country')
    price = models.CharField(max_length=30, null=True, verbose_name='Price')
    price_type = models.CharField(max_length=30, null=True, verbose_name='Price Type')
    category = models.CharField(max_length=30, null=True, verbose_name='Category')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def __unicode__(self):
        return self.title


# 原始ebay分类

class EbayCategory(models.Model):
    cat_id = models.CharField(max_length=32, unique=True, verbose_name='Category ID')
    cat_parent_id = models.CharField(max_length=32, null=True, verbose_name='Category Parent ID')
    name = models.CharField(max_length=128, null=True, verbose_name='Category Name')
    level = models.CharField(max_length=8, null=True, verbose_name='Category Level')
    leaf = models.CharField(max_length=8, null=True, verbose_name='Category Leaf')
    auto_pay = models.CharField(max_length=8, null=True, verbose_name='AutoPayEnabled')
    best_offer = models.CharField(max_length=8, null=True, verbose_name='BestOfferEnabled')

    def __unicode__(self):
        return self.name


# 前端ebay分类

class EbayCategoryForm(models.Model):
    cat_id = models.CharField(max_length=32, unique=True, verbose_name='Category ID')
    cat_name = models.CharField(max_length=128, null=True, verbose_name='Category Name')
    name = models.CharField(max_length=512, null=True, verbose_name='Category Name')
    auto_pay = models.CharField(max_length=8, null=True, verbose_name='AutoPayEnabled')
    best_offer = models.CharField(max_length=8, null=True, verbose_name='BestOfferEnabled')

    def __unicode__(self):
        return self.name


# ebay刊登条目

class EbayProductItem(models.Model):
    product_item = models.ForeignKey(ProductItem)

    item_id = models.CharField(max_length=16, null=True, verbose_name='Item ID')

    account = models.CharField(max_length=32, null=True, verbose_name='Account')
    site_id = models.CharField(max_length=32, null=True, verbose_name='Site ID', default='0')
    list_type = models.CharField(max_length=32, null=True, verbose_name='List Type', default='FixedPriceItem')

    ebay_cat_primary = models.CharField(max_length=32, null=True, verbose_name='Primary Category ID')
    ebay_cat_secondary = models.CharField(max_length=32, null=True, verbose_name='Secondary Category ID')
    store_cat_primary = models.CharField(max_length=32, null=True, verbose_name='Primary Store Category ID')
    store_cat_secondary = models.CharField(max_length=32, null=True, verbose_name='Secondary Store Category ID')

    title = models.CharField(max_length=128, null=True, verbose_name='Title')
    subtitle = models.CharField(max_length=128, null=True, verbose_name='Subtitle')
    describe = models.TextField(null=True, verbose_name='Describe')
    images = models.TextField(null=True, verbose_name='Images')
    images_checked = models.TextField(null=True, verbose_name='Images Checked')
    price = models.CharField(max_length=30, null=True, verbose_name='Price', default='0.00')

    quality = models.CharField(max_length=32, null=True, verbose_name='Quality', default='3')
    duration = models.CharField(max_length=32, null=True, verbose_name='Duration', default='GTC')
    item_location = models.CharField(max_length=32, null=True, verbose_name='Item Location', default='Shenzhen')
    item_country = models.CharField(max_length=32, null=True, verbose_name='Item Country', default='China')
    item_postal = models.CharField(max_length=32, null=True, verbose_name='Item Postal', default='518000')

    payment_method = models.CharField(max_length=128, null=True, verbose_name='Payment Method')
    payment_account = models.CharField(max_length=128, null=True, verbose_name='Payment Account')
    payment_requirement = models.CharField(max_length=128, null=True, verbose_name='Payment Requirement')

    shipping_internal_type = models.CharField(max_length=128, null=True, verbose_name='Shipping Internal Type')
    shipping_international_type = models.CharField(max_length=128, null=True, verbose_name='Shipping International Type')

    dispatch_time_max = models.CharField(max_length=4, null=True, verbose_name='Dispatch Time Max', default='2')

    shipping_internal_service = models.CharField(max_length=128, null=True, verbose_name='Shipping Internal Service')
    shipping_internal_cost = models.CharField(max_length=128, null=True, verbose_name='Shipping Internal Cost', default='0.00')
    shipping_internal_additional_cost = models.CharField(max_length=128, null=True, verbose_name='Shipping Internal Additional Cost', default='2.00')

    shipping_international_service = models.CharField(max_length=128, null=True, verbose_name='Shipping International Service')
    shipping_international_cost = models.CharField(max_length=128, null=True, verbose_name='Shipping International Cost', default='3.00')
    shipping_international_additional_cost = models.CharField(max_length=128, null=True, verbose_name='Shipping International Additional Cost', default='0.00')
    shipping_international_area = models.CharField(max_length=128, null=True, verbose_name='Shipping International Area', default='Worldwide')

    def get_image_list(self):
        return utils.get_image_list(self.images)

    def get_image_checked_list(self):
        return utils.get_image_list(self.images_checked)

    def __unicode__(self):
        return self.title