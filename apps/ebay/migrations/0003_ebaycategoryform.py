# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebay', '0002_ebaycategory'),
    ]

    operations = [
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
    ]
