# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(unique=True, max_length=64, verbose_name=b'Item ID')),
                ('url', models.CharField(max_length=256, null=True, verbose_name=b'URL')),
                ('title', models.CharField(max_length=256, null=True, verbose_name=b'Title')),
                ('content', models.TextField(null=True, verbose_name=b'Content')),
                ('content_url', models.TextField(null=True, verbose_name=b'Content URL')),
                ('images', models.TextField(null=True, verbose_name=b'Images')),
                ('images_checked', models.TextField(null=True, verbose_name=b'Images Checked')),
                ('purchasing_location', models.CharField(max_length=30, null=True, verbose_name=b'Purchasing Location')),
                ('purchasing_price', models.CharField(max_length=30, null=True, verbose_name=b'Purchasing Price')),
                ('purchasing_shipping', models.CharField(max_length=30, null=True, verbose_name=b'Purchasing Shipping')),
                ('retail_price', models.CharField(max_length=30, null=True, verbose_name=b'Retail Price')),
                ('retail_shipping', models.CharField(max_length=30, null=True, verbose_name=b'Retail Shipping')),
                ('category', models.CharField(max_length=128, null=True, verbose_name=b'Category')),
                ('condition', models.CharField(max_length=64, null=True, verbose_name=b'Condition')),
                ('manufacturer', models.CharField(max_length=128, null=True, verbose_name=b'Manufacturer')),
                ('brand', models.CharField(max_length=128, null=True, verbose_name=b'Brand')),
                ('mmn', models.CharField(max_length=128, null=True, verbose_name=b'Manufacturer Model Number')),
                ('sku', models.CharField(max_length=128, null=True, verbose_name=b'SKU')),
                ('product_id', models.CharField(max_length=128, null=True, verbose_name=b'Product ID')),
                ('product_weight', models.CharField(max_length=128, null=True, verbose_name=b'Product Weight')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Time')),
            ],
            options={
                'db_table': 'core_product_item',
            },
            bases=(models.Model,),
        ),
    ]
