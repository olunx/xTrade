# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aliexpress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliexpressstuff',
            name='title',
            field=models.CharField(max_length=256, null=True, verbose_name=b'Title'),
            preserve_default=True,
        ),
    ]
