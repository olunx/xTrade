# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

# Create your views here.


def home(request):
    return render_to_response('index.html')


def hot_stuff(request):
    return render_to_response('hotstuff.html')