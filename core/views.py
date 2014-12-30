# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from scrapy.selector import Selector
# from twisted.internet import reactor
# from scrapy import signals
# from scrapy.crawler import Crawler
# from scrapy.utils.project import get_project_settings
# from xspider.spiders.alibabachina import AlibabachinaSpider

from apps.ebay.models import EbayStuff

# Create your views here.


def home(request):
    return render_to_response('index.html')


def hot_stuff(request):
    category = request.GET.get('category')
    page = request.GET.get('page')

    if category and category != 'None':
        stuffs_list = EbayStuff.objects.filter(category__contains=category).order_by('-sold')
    else:
        category = 0
        stuffs_list = EbayStuff.objects.all().order_by('-sold')

    paginator = Paginator(stuffs_list, 25)
    try:
        stuffs = paginator.page(page)
    except PageNotAnInteger:
        stuffs = paginator.page(1)
    except EmptyPage:
        stuffs = paginator.page(paginator.num_pages)

    return render_to_response('hotstuff.html', {'category': category, 'stuffs': stuffs},
                              context_instance=RequestContext(request))


# def setup_crawler(page):
#     print('setup_crawler page: %s' % page)
#     spider = AlibabachinaSpider(page=page)
#     settings = get_project_settings()
#     crawler = Crawler(settings)
#     crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
#     crawler.configure()
#     crawler.crawl(spider)
#     crawler.start()

ITEM_TITLE = '//*[@id="mod-detail-title"]/h1/text()'
ITEM_PRICE = '//*[@id="mod-detail-price"]/div/table/tr[@class="price"]/td[2]/node()'
ITEM_LOCATION = '//*[@id="mod-detail-bd"]/div[2]/div[6]/div/div/div[2]/div[1]/p[1]/span/text()'
ITEM_SHIPPING = '//*[@id="mod-detail-bd"]/div[2]/div[6]/div/div/div[2]/div[2]/div/div/div/node()'
ITEM_CONTENT = '//*[@id="desc-lazyload-container"]/@data-tfs-url'
ITEM_IMAGE = '//img/@src'


def parse_content(url):
    # print('url: %s' % url)
    response = requests.get(url)
    if response and response.status_code == 200:
        data = response.text[10:-3]
        # print('response: %s' % data)
        return data
    return ''


def scrap_page(request):
    page = request.GET.get('page')
    if page:
        response = requests.get(page)
        content_sel = Selector(text=response.text)
        title = content_sel.xpath(ITEM_TITLE)
        price = content_sel.xpath(ITEM_PRICE)
        location = content_sel.xpath(ITEM_LOCATION)
        shipping = content_sel.xpath(ITEM_SHIPPING)
        content_url = content_sel.xpath(ITEM_CONTENT).extract()
        if content_url and len(content_url) > 0:
            content_data = parse_content(content_url[0])
            content_sel = Selector(text=content_data)
            images = content_sel.xpath('//img/@src')
            content_text = content_sel.xpath('//p/text()')
        print(title.extract())
        print(price.extract())
        print(location.extract())
        print(shipping.extract())
        print(images.extract())
        print(content_text.extract())
        # setup_crawler(page)
        # from twisted.internet import reactor
        # print('reactor.run()')
        # reactor.run()
        # from scrapy.cmdline import execute
        # execute(['scrapy', 'crawl', 'alibabachina', 'domain=http://detail.1688.com/offer/42326799135.html'])
    return render_to_response('scrapy.html')