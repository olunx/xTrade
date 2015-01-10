# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EbayCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_id', models.CharField(unique=True, max_length=32, verbose_name=b'Category ID')),
                ('cat_parent_id', models.CharField(max_length=32, null=True, verbose_name=b'Category Parent ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name=b'Category Name')),
                ('level', models.CharField(max_length=8, null=True, verbose_name=b'Category Level')),
                ('leaf', models.CharField(max_length=8, null=True, verbose_name=b'Category Leaf')),
                ('auto_pay', models.CharField(max_length=8, null=True, verbose_name=b'AutoPayEnabled')),
                ('best_offer', models.CharField(max_length=8, null=True, verbose_name=b'BestOfferEnabled')),
            ],
            options={
                'db_table': 'apps_ebay_category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EbayCategoryForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_id', models.CharField(unique=True, max_length=32, verbose_name=b'Category ID')),
                ('cat_name', models.CharField(max_length=128, null=True, verbose_name=b'Category Name')),
                ('name', models.CharField(max_length=512, null=True, verbose_name=b'Category Name')),
                ('auto_pay', models.CharField(max_length=8, null=True, verbose_name=b'AutoPayEnabled')),
                ('best_offer', models.CharField(max_length=8, null=True, verbose_name=b'BestOfferEnabled')),
            ],
            options={
                'db_table': 'apps_ebay_category_form',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EbayProductItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(max_length=16, null=True, verbose_name=b'Item ID')),
                ('account', models.CharField(max_length=32, null=True, verbose_name=b'Account')),
                ('site_id', models.CharField(default=b'0', max_length=32, null=True, verbose_name=b'Site ID')),
                ('list_type', models.CharField(default=b'FixedPriceItem', max_length=32, null=True, verbose_name=b'List Type')),
                ('ebay_cat_primary', models.CharField(max_length=32, null=True, verbose_name=b'Primary Category ID')),
                ('ebay_cat_secondary', models.CharField(max_length=32, null=True, verbose_name=b'Secondary Category ID')),
                ('store_cat_primary', models.CharField(max_length=32, null=True, verbose_name=b'Primary Store Category ID')),
                ('store_cat_secondary', models.CharField(max_length=32, null=True, verbose_name=b'Secondary Store Category ID')),
                ('title', models.CharField(max_length=128, null=True, verbose_name=b'Title')),
                ('subtitle', models.CharField(max_length=128, null=True, verbose_name=b'Subtitle')),
                ('describe', models.TextField(null=True, verbose_name=b'Describe')),
                ('images', models.TextField(null=True, verbose_name=b'Images')),
                ('images_checked', models.TextField(null=True, verbose_name=b'Images Checked')),
                ('price', models.CharField(default=b'0.00', max_length=30, null=True, verbose_name=b'Price')),
                ('quality', models.CharField(default=b'3', max_length=32, null=True, verbose_name=b'Quality')),
                ('duration', models.CharField(default=b'GTC', max_length=32, null=True, verbose_name=b'Duration')),
                ('item_location', models.CharField(default=b'Shenzhen', max_length=32, null=True, verbose_name=b'Item Location')),
                ('item_country', models.CharField(default=b'China', max_length=32, null=True, verbose_name=b'Item Country')),
                ('item_postal', models.CharField(default=b'518000', max_length=32, null=True, verbose_name=b'Item Postal')),
                ('payment_method', models.CharField(default=b'PayPal', max_length=128, null=True, verbose_name=b'Payment Method')),
                ('payment_account', models.CharField(default=b'xieshizheng07@gmail.com', max_length=128, null=True, verbose_name=b'Payment Account')),
                ('payment_requirement', models.CharField(max_length=128, null=True, verbose_name=b'Payment Requirement')),
                ('shipping_internal_type', models.CharField(max_length=128, null=True, verbose_name=b'Shipping Internal Type')),
                ('shipping_international_type', models.CharField(max_length=128, null=True, verbose_name=b'Shipping International Type')),
                ('dispatch_time_max', models.CharField(default=b'2', max_length=4, null=True, verbose_name=b'Dispatch Time Max')),
                ('shipping_internal_service', models.CharField(max_length=128, null=True, verbose_name=b'Shipping Internal Service')),
                ('shipping_internal_cost', models.CharField(default=b'0.00', max_length=128, null=True, verbose_name=b'Shipping Internal Cost')),
                ('shipping_internal_additional_cost', models.CharField(default=b'0.00', max_length=128, null=True, verbose_name=b'Shipping Internal Additional Cost')),
                ('shipping_international_service', models.CharField(max_length=128, null=True, verbose_name=b'Shipping International Service')),
                ('shipping_international_cost', models.CharField(default=b'3.00', max_length=128, null=True, verbose_name=b'Shipping International Cost')),
                ('shipping_international_additional_cost', models.CharField(default=b'0.00', max_length=128, null=True, verbose_name=b'Shipping International Additional Cost')),
                ('shipping_international_area', models.CharField(default=b'Worldwide', max_length=128, null=True, verbose_name=b'Shipping International Area')),
                ('product_item', models.ForeignKey(to='core.ProductItem')),
            ],
            options={
                'db_table': 'apps_ebay_product_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EbayStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(unique=True, max_length=30, verbose_name=b'Ebay ID')),
                ('url', models.CharField(max_length=256, null=True, verbose_name=b'URL')),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'Title')),
                ('subtitle', models.CharField(max_length=100, null=True, verbose_name=b'Subtitle')),
                ('sold', models.IntegerField(null=True, verbose_name=b'Sold')),
                ('watching', models.IntegerField(null=True, verbose_name=b'Watching')),
                ('country', models.CharField(max_length=30, null=True, verbose_name=b'Country')),
                ('price', models.CharField(max_length=30, null=True, verbose_name=b'Price')),
                ('price_type', models.CharField(max_length=30, null=True, verbose_name=b'Price Type')),
                ('category', models.CharField(max_length=30, null=True, verbose_name=b'Category')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Time')),
            ],
            options={
                'db_table': 'apps_ebay_stuff',
            },
            bases=(models.Model,),
        ),
    ]
