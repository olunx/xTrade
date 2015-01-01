# -*- coding: utf-8 -*-
__author__ = 'olunx'

import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector

from apps.alibabachina.models import AlibabachinaScrapy

ITEM_TITLE = '//*[@id="mod-detail-title"]/h1/text()'
ITEM_PRICE = '//*[@id="mod-detail-price"]/div/table/tr[@class="price"]/td[2]/node()'
ITEM_LOCATION = '//*[@id="mod-detail-bd"]/div[2]/div[6]/div/div/div[2]/div[1]/p[1]/span/text()'
ITEM_SHIPPING = '//*[@id="mod-detail-bd"]/div[2]/div[6]/div/div/div[2]/div[2]/div/div/div/node()'
ITEM_CONTENT = '//*[@id="desc-lazyload-container"]/@data-tfs-url'
ITEM_IMAGE = '//img/@src'
ITEM_CONTENT_TEXT = '//p/node()'


def get_text_by_list(item):
    if item and len(item) > 0:
        return ' '.join(x.strip() for x in item).strip()
    return ''


def get_text(item):
    if item and len(item) > 0:
        return item[0]
    return ''


def get_text_content(item):
    data = ''
    if item:
        for i in item:
            text = BeautifulSoup(i).get_text().strip()
            if text and text != "":
                data += '<p>%s</p>' % text
    return data


def parse_content(url):
    response = requests.get(url)
    if response and response.status_code == 200:
        data = response.text[10:-3]
        return data
    return ''


def scrap_page(page):
    response = requests.get(page)
    content_sel = Selector(text=response.text)
    title = content_sel.xpath(ITEM_TITLE).extract()
    price = content_sel.xpath(ITEM_PRICE).extract()
    location = content_sel.xpath(ITEM_LOCATION).extract()
    shipping = content_sel.xpath(ITEM_SHIPPING).extract()
    content_url = content_sel.xpath(ITEM_CONTENT).extract()
    if content_url and len(content_url) > 0:
        content_data = parse_content(content_url[0])
        content_sel = Selector(text=content_data)
        images = content_sel.xpath(ITEM_IMAGE).extract()
        content_text = content_sel.xpath(ITEM_CONTENT_TEXT).extract()

    # process text
    title = get_text(title)
    price = BeautifulSoup(get_text_by_list(price)).get_text()
    location = get_text(location)
    shipping = BeautifulSoup(get_text_by_list(shipping)).get_text()
    content_text = get_text_content(content_text)

    print(title)
    print(price)
    print(location)
    print(shipping)
    print(images)
    print(content_text)
    try:
        item = AlibabachinaScrapy.objects.get(url=page)
    except AlibabachinaScrapy.DoesNotExist:
        item = AlibabachinaScrapy(
            url=page,
            title=title,
            price=price,
            location=location,
            shipping=shipping,
            image=images,
            content=content_text,
            content_url=content_url
        )
        item.save()
    else:
        item.title = title
        item.price = price
        item.location = location
        item.shipping = shipping
        item.image = images
        item.content = content_text
        item.content_url = content_url
        item.save()