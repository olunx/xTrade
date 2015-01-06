# -*- coding: utf-8 -*-
__author__ = 'olunx'

import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector

from core.models import ProductItem
from core import utils as core_utils

ITEM_TITLE = '//*[@id="mod-detail-title"]/h1/text()'
ITEM_PRICE = '//*[@id="mod-detail-price"]/div/table/tr[@class="price"]/td[2]/node()'
ITEM_LOCATION = '//*[@id="mod-detail-bd"]/div[2]/div[6]/div/div/div[2]/div[1]/p[1]/span/text()'
ITEM_SHIPPING = '//*[@id="mod-detail-bd"]/div[2]/div[6]/div/div/div[2]/div[2]/div/div/div/node()'
ITEM_CONTENT = '//*[@id="desc-lazyload-container"]/@data-tfs-url'
ITEM_IMAGE = '//img/@src'
ITEM_CONTENT_TEXT = '//p/node()'


class ListingItem():

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

    def get_text_content(self, item):
        data = ''
        if item:
            for i in item:
                text = BeautifulSoup(i).get_text().strip()
                if text and text != "":
                    data += '<p>%s</p>' % text
        return data

    def parse_content(self, url):
        response = requests.get(url)
        if response and response.status_code == 200:
            data = response.text[10:-3]
            return data
        return ''

    def scrap_page(self, page):
        response = requests.get(page)
        content_sel = Selector(text=response.text)
        title = content_sel.xpath(ITEM_TITLE).extract()
        price = content_sel.xpath(ITEM_PRICE).extract()
        location = content_sel.xpath(ITEM_LOCATION).extract()
        shipping = content_sel.xpath(ITEM_SHIPPING).extract()
        content_url = content_sel.xpath(ITEM_CONTENT).extract()
        if content_url and len(content_url) > 0:
            content_data = self.parse_content(content_url[0])
            content_sel = Selector(text=content_data)
            images = content_sel.xpath(ITEM_IMAGE).extract()
            content_text = content_sel.xpath(ITEM_CONTENT_TEXT).extract()

        # process text
        title = self.get_text(title)
        price = BeautifulSoup(self.get_text_by_list(price)).get_text()
        location = self.get_text(location)
        shipping = BeautifulSoup(self.get_text_by_list(shipping)).get_text()
        content_text = self.get_text_content(content_text)

        print(title)
        print(price)
        print(location)
        print(shipping)
        print(images)
        print(content_text)
        try:
            item = ProductItem.objects.get(url=page)
        except ProductItem.DoesNotExist:
            item = ProductItem(
                item_id=core_utils.get_time_stamp(),
                url=page,
                title=title,
                image=images,
                content=content_text,
                content_url=content_url,
                purchasing_price=price,
                purchasing_location=location,
                purchasing_shipping=shipping,
            )
            item.save()
        else:
            item.title = title
            item.image = images
            item.content = content_text
            item.content_url = content_url
            item.purchasing_price = price
            item.purchasing_location = location
            item.purchasing_shipping = shipping
            item.save()