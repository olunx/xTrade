# -*- coding: utf-8 -*-
__author__ = 'olunx'

from django.test import TestCase
# Create your tests here.

import goslate


def main():
    gs = goslate.Goslate()
    print gs.translate('可弯曲钥匙扣数据线 创意Micro USB钥匙扣充电线 母座正反可插', 'en')


if __name__ == '__main__':
    main()