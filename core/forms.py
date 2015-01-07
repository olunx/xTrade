# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.forms import ModelForm

from core.models import ProductItem


class ProductItemForm(ModelForm):
    class Meta:
        model = ProductItem
        fields = ['title', 'content', 'purchasing_location', 'purchasing_price', 'purchasing_shipping']