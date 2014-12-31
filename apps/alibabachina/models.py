# -*- coding: utf-8 -*-
__author__ = 'olunx'

import ast
from django.db import models


class AlibabachinaScrapy(models.Model):
    url = models.CharField(max_length=256, null=True, verbose_name='URL')
    title = models.CharField(max_length=256, null=True, verbose_name='Title')
    content_url = models.TextField(null=True, verbose_name='Content')
    content = models.TextField(null=True, verbose_name='Content')
    image = models.TextField(null=True, verbose_name='Image')
    location = models.CharField(max_length=30, null=True, verbose_name='Image')
    shipping = models.CharField(max_length=30, null=True, verbose_name='Shipping')
    price = models.CharField(max_length=30, null=True, verbose_name='Price')
    sold = models.IntegerField(null=True, verbose_name='Sold')
    category = models.CharField(max_length=30, null=True, verbose_name='Category')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def get_image_list(self):
        data = []
        if self.image:
            data = ast.literal_eval(self.image)
        return list(set(data))

    def __unicode__(self):
        return self.title