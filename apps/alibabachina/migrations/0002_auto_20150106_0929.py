# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alibabachina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alibabachinascrapy',
            name='content',
            field=models.TextField(null=True, verbose_name=b'Content URL'),
            preserve_default=True,
        ),
    ]
