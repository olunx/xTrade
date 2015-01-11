# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AliexpressStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(unique=True, max_length=64, verbose_name=b'Item ID')),
                ('url', models.CharField(max_length=256, null=True, verbose_name=b'URL')),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'Title')),
                ('price', models.CharField(max_length=30, null=True, verbose_name=b'Price')),
                ('unit', models.CharField(max_length=128, null=True, verbose_name=b'Unit')),
                ('min_order', models.CharField(max_length=128, null=True, verbose_name=b'Min Order')),
                ('shipping', models.CharField(max_length=128, null=True, verbose_name=b'Shipping')),
                ('rate_num', models.IntegerField(null=True, verbose_name=b'Rate Num')),
                ('order_num', models.IntegerField(null=True, verbose_name=b'Order Num')),
                ('store_name', models.CharField(max_length=256, null=True, verbose_name=b'Store Name')),
                ('store_url', models.CharField(max_length=256, null=True, verbose_name=b'Store URL')),
                ('category', models.CharField(max_length=30, null=True, verbose_name=b'Category')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Time')),
            ],
            options={
                'db_table': 'apps_aliexpress_stuff',
            },
            bases=(models.Model,),
        ),
    ]
