# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.db import models


# 爬虫数据对象

class AlibabaChinaStuff(models.Model):
    item_id = models.CharField(max_length=64, unique=True, verbose_name='Item ID')
    url = models.CharField(max_length=256, null=True, verbose_name='URL')
    title = models.CharField(max_length=100, null=True, verbose_name='Title')

    company_name = models.CharField(max_length=128, null=True, verbose_name='Company Name')
    company_id = models.CharField(max_length=128, null=True, verbose_name='Company ID')
    company_url = models.CharField(max_length=128, null=True, verbose_name='Company URL')
    company_location = models.CharField(max_length=128, null=True, verbose_name='Company Location')

    sold_item = models.IntegerField(null=True, verbose_name='Sold Item')
    sold_person = models.IntegerField(null=True, verbose_name='Sold Person')

    price = models.CharField(max_length=30, null=True, verbose_name='Price')
    category = models.CharField(max_length=30, null=True, verbose_name='Category')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'apps_alibaba_china_stuff'