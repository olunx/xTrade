# -*- coding: utf-8 -*-

import ast
from django.db import models


class ProductItem(models.Model):
    item_id = models.CharField(max_length=64, unique=True, verbose_name='Item ID')
    url = models.CharField(max_length=256, null=True, verbose_name='URL')
    title = models.CharField(max_length=256, null=True, verbose_name='Title')
    content = models.TextField(null=True, verbose_name='Content')
    content_url = models.TextField(null=True, verbose_name='Content URL')
    images = models.TextField(null=True, verbose_name='Image')

    purchasing_location = models.CharField(max_length=30, null=True, verbose_name='Purchasing Location')
    purchasing_price = models.CharField(max_length=30, null=True, verbose_name='Purchasing Price')
    purchasing_shipping = models.CharField(max_length=30, null=True, verbose_name='Purchasing Shipping')
    
    retail_price = models.CharField(max_length=30, null=True, verbose_name='Retail Price')
    retail_shipping = models.CharField(max_length=30, null=True, verbose_name='Retail Shipping')

    category = models.CharField(max_length=128, null=True, verbose_name='Category')
    condition = models.CharField(max_length=64, null=True, verbose_name='Condition')
    manufacturer = models.CharField(max_length=128, null=True, verbose_name='Manufacturer')
    brand = models.CharField(max_length=128, null=True, verbose_name='Brand')
    mmn = models.CharField(max_length=128, null=True, verbose_name='Manufacturer Model Number')

    sku = models.CharField(max_length=128, null=True, verbose_name='SKU')
    product_id = models.CharField(max_length=128, null=True, verbose_name='Product ID')
    product_weight = models.CharField(max_length=128, null=True, verbose_name='Product Weight')

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def get_image_list(self):
        data = []
        if self.images:
            data = ast.literal_eval(self.images)
        return list(set(data))

    def __unicode__(self):
        return self.title

