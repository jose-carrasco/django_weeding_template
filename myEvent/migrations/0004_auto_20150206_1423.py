# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myEvent', '0003_auto_20150129_1739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='guest',
            options={'verbose_name': 'Invitado', 'verbose_name_plural': 'Invitados'},
        ),
        migrations.AlterField(
            model_name='guest',
            name='confirmation_date',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha de confirmaci\xc3\xb3n', blank=True),
            preserve_default=True,
        ),
    ]
