# -*- coding: utf-8 -*-
__author__ = 'olunx'

import re
import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector

from core.models import ProductItem
from core import utils as core_utils

ITEM_TITLE = '//h1[@class="product-name"]/text()'
ITEM_PRICE = '//*[@id="sku-price"]/text()'
ITEM_CONTENT_URL = 'window\.runParams\.descUrl="(.*?)";'
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

    def parse_content(self, url):
        response = requests.get(url)
        if response and response.status_code == 200:
            data = response.text.replace("window.productDescription='", '').strip()[:-3]
            return data
        return ''

    def scrap_page(self, page):
        response = requests.get(page)
        selector = Selector(text=response.text)
        title = selector.xpath(ITEM_TITLE).extract()
        price = selector.xpath(ITEM_PRICE).extract()

        content_url = re.findall(ITEM_CONTENT_URL, response.text)
        if content_url and len(content_url) > 0:
            content_data = self.parse_content(content_url[0])
            content_sel = Selector(text=content_data)
            images = content_sel.xpath(ITEM_IMAGE).extract()
            content = content_data

        # process text
        title = self.get_text(title)
        price = self.get_text_by_list(price)
        price = BeautifulSoup(price).get_text()
        images = core_utils.remove_url_query_list(images)

        print(title)
        print(price)
        print(images)
        print(content)
        try:
            item = ProductItem.objects.get(url=page)
        except ProductItem.DoesNotExist:
            item = ProductItem(
                item_id=core_utils.get_time_stamp(),
                url=page,
                title=title,
                images=images,
                content=content,
                purchasing_price=price,
            )
            item.save()
            return item.id
        else:
            item.title = title
            item.images = images
            item.images_checked = None
            item.content = content
            item.purchasing_price = price
            item.save()
            return item.id