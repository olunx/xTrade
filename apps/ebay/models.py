# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.db import models

from core.models import ProductItem


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


# ebay刊登条目

class EbayProductItem(ProductItem):
    ebay_account = models.CharField(max_length=32, null=True, verbose_name='Account')
    ebay_site_id = models.CharField(max_length=32, null=True, verbose_name='Site ID')
    ebay_list_type = models.IntegerField(null=True, verbose_name='List Type')

    ebay_cat_primary = models.CharField(max_length=32, null=True, verbose_name='Primary Category ID')
    ebay_cat_secondary = models.CharField(max_length=32, null=True, verbose_name='Secondary Category ID')
    store_cat_primary = models.CharField(max_length=32, null=True, verbose_name='Primary Store Category ID')
    store_cat_secondary = models.CharField(max_length=32, null=True, verbose_name='Secondary Store Category ID')

    ebay_quality = models.CharField(max_length=32, null=True, verbose_name='Quality')
    ebay_duration = models.CharField(max_length=32, null=True, verbose_name='Duration')
    ebay_item_location = models.CharField(max_length=32, null=True, verbose_name='Item Location')
    ebay_item_country = models.CharField(max_length=32, null=True, verbose_name='Item Location')
    ebay_item_postal = models.CharField(max_length=32, null=True, verbose_name='Item Postal')

    def __unicode__(self):
        return self.title


#  原始ebay分类

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