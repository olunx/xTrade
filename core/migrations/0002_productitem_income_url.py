# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='income_url',
            field=models.CharField(max_length=256, null=True, verbose_name=b'Income URL'),
            preserve_default=True,
        ),
    ]
