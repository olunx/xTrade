# -*- coding: utf-8 -*-
__author__ = 'olunx'

import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector

from core.models import ProductItem
from core import utils as core_utils

ITEM_TITLE = '//*[@class="ls-icon ls-brief"]/h1/text()'
ITEM_PRICE = '//*[@class="ls-icon ls-brief"]/table/tr[1]/td/span/node()'
ITEM_LOCATION = '//*[@class="ls-icon ls-brief"]/table/tr[4]/td/text()'
ITEM_DETAIL = '//*[@id="J-product-detail"]/div[@class="box box-first"]/table'
ITEM_CONTENT = '//*[@id="J-rich-text-description"]/node()'
ITEM_IMAGE = '//img/@src'


class ListingScrap():

    def __init__(self):
        pass

    def get_text_by_list(self, item):
        if item and len(item) > 0:
            return ' '.join(x.strip() for x in item).strip()
        return ''

    def get_text(self, item):
        if item and len(item) > 0:
            return item[0]
        return ''

    def scrap_page(self, page):
        response = requests.get(page)
        selector = Selector(text=response.text)
        title = selector.xpath(ITEM_TITLE).extract()
        price = selector.xpath(ITEM_PRICE).extract()
        location = selector.xpath(ITEM_LOCATION).extract()
        detail = selector.xpath(ITEM_DETAIL).extract()
        content = selector.xpath(ITEM_CONTENT).extract()
        content = self.get_text_by_list(content)
        content_sel = Selector(text=content)
        images = content_sel.xpath(ITEM_IMAGE).extract()

        # process text
        title = self.get_text(title)
        price = self.get_text_by_list(price)
        price = BeautifulSoup(price).get_text()
        location = self.get_text(location)
        detail = self.get_text_by_list(detail)
        images = core_utils.remove_url_query_list(images)
        content_text = '%s<br>%s' % (detail, content)

        print(title)
        print(price)
        print(location)
        print(detail)
        print(images)
        print(content_text)
        try:
            item = ProductItem.objects.get(url=page)
        except ProductItem.DoesNotExist:
            item = ProductItem(
                item_id=core_utils.get_time_stamp(),
                url=page,
                title=title,
                images=images,
                content=content_text,
                purchasing_price=price,
                purchasing_location=location,
            )
            item.save()
            return item.id
        else:
            item.title = title
            item.images = images
            item.images_checked = None
            item.content = content_text
            item.purchasing_price = price
            item.purchasing_location = location
            item.save()
            return item.id