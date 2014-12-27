# -*- coding: utf-8 -*-

from django.db import models


class EbayStuff(models.Model):
    ebay_id = models.CharField(max_length=30, unique=True, verbose_name='Ebay ID')
    title = models.CharField(max_length=100, verbose_name='Title')
    sold = models.CharField(max_length=10, verbose_name='Sold')
    watching = models.CharField(max_length=10, verbose_name='Watching')
    country = models.CharField(max_length=30, verbose_name='Country')
    price = models.CharField(max_length=30, verbose_name='Price')
    price_type = models.CharField(max_length=30, verbose_name='Price Type')
    category = models.CharField(max_length=30, verbose_name='Category')
    create_date = models.DateTimeField(verbose_name='Create Time')