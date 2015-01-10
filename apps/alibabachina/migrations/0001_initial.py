# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlibabaChinaStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(unique=True, max_length=64, verbose_name=b'Item ID')),
                ('url', models.CharField(max_length=256, null=True, verbose_name=b'URL')),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'Title')),
                ('company_name', models.CharField(max_length=128, null=True, verbose_name=b'Company Name')),
                ('company_id', models.CharField(max_length=128, null=True, verbose_name=b'Company ID')),
                ('company_url', models.CharField(max_length=128, null=True, verbose_name=b'Company URL')),
                ('company_location', models.CharField(max_length=128, null=True, verbose_name=b'Company Location')),
                ('sold_item', models.IntegerField(null=True, verbose_name=b'Sold Item')),
                ('sold_person', models.IntegerField(null=True, verbose_name=b'Sold Person')),
                ('price', models.CharField(max_length=30, null=True, verbose_name=b'Price')),
                ('category', models.CharField(max_length=30, null=True, verbose_name=b'Category')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Time')),
            ],
            options={
                'db_table': 'apps_alibaba_china_stuff',
            },
            bases=(models.Model,),
        ),
    ]
