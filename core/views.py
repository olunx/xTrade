# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.models import EbayStuff

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