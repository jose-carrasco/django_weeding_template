# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myEvent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
