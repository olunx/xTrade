# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
    ]
