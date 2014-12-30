# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlibabachinaScrapy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=256, null=True, verbose_name=b'URL')),
                ('title', models.CharField(max_length=256, null=True, verbose_name=b'Title')),
                ('content_url', models.TextField(null=True, verbose_name=b'Content')),
                ('content', models.TextField(null=True, verbose_name=b'Content')),
                ('image', models.TextField(null=True, verbose_name=b'Image')),
                ('location', models.CharField(max_length=30, null=True, verbose_name=b'Image')),
                ('shipping', models.CharField(max_length=30, null=True, verbose_name=b'Shipping')),
                ('price', models.CharField(max_length=30, null=True, verbose_name=b'Price')),
                ('sold', models.IntegerField(null=True, verbose_name=b'Sold')),
                ('category', models.CharField(max_length=30, null=True, verbose_name=b'Category')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Create Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
