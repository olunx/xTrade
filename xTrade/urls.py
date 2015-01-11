from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    url(r'^$', 'core.views.home'),
    url(r'^hot/item/ebay/$', 'core.views.hot_item_ebay', {'category': 0, 'page': 1}),
    url(r'^hot/item/ebay/(\d+)/$', 'core.views.hot_item_ebay', {'page': 1}),
    url(r'^hot/item/ebay/(\d+)/(\d+)/$', 'core.views.hot_item_ebay'),

    url(r'^hot/item/alibabachina/$', 'core.views.hot_item_alibabachina', {'category': 0, 'page': 1}),
    url(r'^hot/item/alibabachina/(\d+)/$', 'core.views.hot_item_alibabachina', {'page': 1}),
    url(r'^hot/item/alibabachina/(\d+)/(\d+)/$', 'core.views.hot_item_alibabachina'),

    url(r'^hot/item/aliexpress/$', 'core.views.hot_item_aliexpress', {'category': 0, 'page': 1}),
    url(r'^hot/item/aliexpress/(\d+)/$', 'core.views.hot_item_aliexpress', {'page': 1}),
    url(r'^hot/item/aliexpress/(\d+)/(\d+)/$', 'core.views.hot_item_aliexpress'),

    url(r'^listing/$', 'core.views.listing_list'),
    url(r'^listing/detail/(\d+)/$', 'core.views.listing_detail'),
    url(r'^listing/detail/new/$', 'core.views.listing_detail_new'),
    url(r'^listing/detail/create/$', 'core.views.listing_detail_create'),
    url(r'^listing/detail/save/$', 'core.views.listing_detail_save'),

    url(r'^listing/detail/ebay/(\d+)/$', 'core.views.listing_detail_ebay'),
    url(r'^listing/detail/ebay/create/$', 'core.views.listing_detail_ebay_create'),
    url(r'^listing/detail/ebay/save/$', 'core.views.listing_detail_ebay_save'),
    url(r'^listing/detail/ebay/list/$', 'core.views.listing_detail_ebay_list'),

    url(r'^api/translate/', 'core.utils.translate'),
    url(r'^api/gen_category/', 'apps.ebay.views.gen_category'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
