# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.db import models


# 爬虫数据对象

class AliexpressStuff(models.Model):
    item_id = models.CharField(max_length=64, unique=True, verbose_name='Item ID')
    url = models.CharField(max_length=256, null=True, verbose_name='URL')
    title = models.CharField(max_length=256, null=True, verbose_name='Title')

    price = models.CharField(max_length=30, null=True, verbose_name='Price')
    unit = models.CharField(max_length=128, null=True, verbose_name='Unit')
    min_order = models.CharField(max_length=128, null=True, verbose_name='Min Order')

    shipping = models.CharField(max_length=128, null=True, verbose_name='Shipping')

    rate_num = models.IntegerField(null=True, verbose_name='Rate Num')
    order_num = models.IntegerField(null=True, verbose_name='Order Num')

    store_name = models.CharField(max_length=256, null=True, verbose_name='Store Name')
    store_url = models.CharField(max_length=256, null=True, verbose_name='Store URL')

    category = models.CharField(max_length=30, null=True, verbose_name='Category')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'apps_aliexpress_stuff'