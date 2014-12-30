# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
            },
            bases=(models.Model,),
        ),
    ]
