# -*- coding: utf-8 -*-
__author__ = 'olunx'

import json

from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading

from apps.ebay.models import EbayCategory, EbayCategoryForm

from django.db.models import Count
from django.conf import settings


def fetch_categories():
    try:
        api = Trading(domain='api.sandbox.ebay.com', config_file=settings.FILE_EBAY_API_CONFIG, warnings=True, timeout=20, siteid=101)

        callData = {
            'DetailLevel': 'ReturnAll',
            'CategorySiteID': 0,
            'LevelLimit': 4,
        }

        api.execute('GetCategories', callData)
        result = api.response.json()
        result = json.loads(result)
        category = result.get('CategoryArray').get('Category')
        EbayCategory.objects.all().delete()
        for cat in category:
            try:
                item = EbayCategory.objects.get(cat_id=cat.get('CategoryID'))
            except EbayCategory.DoesNotExist:
                item = EbayCategory()
                item.cat_id = cat.get('CategoryID')
                item.cat_parent_id = cat.get('CategoryParentID')
                item.name = cat.get('CategoryName')
                item.leaf = cat.get('LeafCategory')
                item.level = cat.get('CategoryLevel')
                item.auto_pay = cat.get('AutoPayEnabled')
                item.best_offer = cat.get('BestOfferEnabled')
                item.save()
            else:
                pass

    except ConnectionError as e:
        print(e)
        print(e.response.dict())


'''
只读取4层分类，实际上最多有5层。
'''


def gen_categories():
    level_one_items = EbayCategory.objects.filter(level='1')
    for level_one in level_one_items:
        if level_one.leaf != 'true':
            level_two_items = EbayCategory.objects.filter(level='2', cat_parent_id=level_one.cat_id)
            for level_two in level_two_items:
                if level_two.leaf != 'true':
                    level_three_items = EbayCategory.objects.filter(level='3', cat_parent_id=level_two.cat_id)
                    for level_three in level_three_items:
                        if level_three.leaf != 'true':
                            level_four_items = EbayCategory.objects.filter(level='4', cat_parent_id=level_three.cat_id)
                            for level_four in level_four_items:
                                if level_four.leaf != 'true':
                                    print '%s is not the leaf' % level_four.name
                                else:
                                    name = '%s > %s > %s > %s' % (level_one.name, level_two.name, level_three.name, level_four.name)
                                    EbayCategoryForm.objects.create(cat_id=level_four.cat_id, cat_name=level_one.name, name=name, auto_pay=level_four.auto_pay, best_offer=level_four.best_offer)
                        else:
                            name = '%s > %s > %s' % (level_one.name, level_two.name, level_three.name)
                            EbayCategoryForm.objects.create(cat_id=level_three.cat_id, cat_name=level_one.name, name=name, auto_pay=level_three.auto_pay, best_offer=level_three.best_offer)
                else:
                    name = '%s > %s ' % (level_one.name, level_two.name)
                    EbayCategoryForm.objects.create(cat_id=level_two.cat_id, cat_name=level_one.name, name=name, auto_pay=level_two.auto_pay, best_offer=level_two.best_offer)
        else:
            print '%s' % level_one.name


def get_categories():
    result = {}
    items = EbayCategoryForm.objects.values('cat_name').annotate(Count('cat_id'))
    for item in items:
        cats = EbayCategoryForm.objects.filter(cat_name=item['cat_name'])
        # print cats
        result[item['cat_name']] = cats
    return result