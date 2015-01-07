from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    url(r'^$', 'core.views.home'),
    url(r'^hotstuff/', 'core.views.hot_stuff'),
    url(r'^listing/$', 'core.views.listing_list'),

    url(r'^listing/detail/(\d+)/$', 'core.views.listing_detail'),
    url(r'^listing/detail/create/$', 'core.views.listing_detail_create'),
    url(r'^listing/detail/save/$', 'core.views.listing_detail_save'),

    url(r'^listing/detail/ebay/(\d+)/$', 'core.views.listing_detail_ebay'),
    url(r'^listing/detail/ebay/create/$', 'core.views.listing_detail_ebay_create'),
    url(r'^listing/detail/ebay/save/$', 'core.views.listing_detail_ebay_save'),

    url(r'^api/translate/', 'core.utils.translate'),
    url(r'^api/gen_category/', 'apps.ebay.views.gen_category'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
