# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myEvent', '0002_auto_20150122_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500, verbose_name=b'Descripci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name=b'Habilitado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='register_date',
            field=models.DateTimeField(verbose_name=b'Fecha de registro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='code',
            field=models.CharField(max_length=5, verbose_name=b'C\xc3\xb3digo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='confirmation_date',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha de confirmaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfHa confirmado?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.CharField(max_length=100, verbose_name=b'Correo electr\xc3\xb3nico'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name=b'Habilitado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name=b'Apellido'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='quantity_assigned',
            field=models.IntegerField(default=1, verbose_name=b'Boletos asignados'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='quantity_confirmed',
            field=models.IntegerField(default=0, verbose_name=b'Boletos confirmados'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='register_date',
            field=models.DateTimeField(verbose_name=b'Fecha de registro'),
            preserve_default=True,
        ),
    ]
