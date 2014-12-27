from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    url(r'^$', 'core.views.home'),
    url(r'^hotstuff/', 'core.views.hot_stuff'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
