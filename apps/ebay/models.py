# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.db import models


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