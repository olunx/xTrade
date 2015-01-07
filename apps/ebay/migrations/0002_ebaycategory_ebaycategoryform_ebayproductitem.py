# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('ebay', '0001_initial'),
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
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EbayProductItem',
            fields=[
                ('productitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.ProductItem')),
                ('ebay_account', models.CharField(max_length=32, null=True, verbose_name=b'Account')),
                ('ebay_site_id', models.CharField(max_length=32, null=True, verbose_name=b'Site ID')),
                ('ebay_list_type', models.IntegerField(null=True, verbose_name=b'List Type')),
                ('ebay_cat_primary', models.CharField(max_length=32, null=True, verbose_name=b'Primary Category ID')),
                ('ebay_cat_secondary', models.CharField(max_length=32, null=True, verbose_name=b'Secondary Category ID')),
                ('store_cat_primary', models.CharField(max_length=32, null=True, verbose_name=b'Primary Store Category ID')),
                ('store_cat_secondary', models.CharField(max_length=32, null=True, verbose_name=b'Secondary Store Category ID')),
                ('ebay_quality', models.CharField(max_length=32, null=True, verbose_name=b'Quality')),
                ('ebay_duration', models.CharField(max_length=32, null=True, verbose_name=b'Duration')),
                ('ebay_item_location', models.CharField(max_length=32, null=True, verbose_name=b'Item Location')),
                ('ebay_item_country', models.CharField(max_length=32, null=True, verbose_name=b'Item Location')),
                ('ebay_item_postal', models.CharField(max_length=32, null=True, verbose_name=b'Item Postal')),
            ],
            options={
            },
            bases=('core.productitem',),
        ),
    ]
