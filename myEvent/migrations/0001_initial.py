# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('enabled', models.BooleanField()),
                ('active', models.BooleanField()),
                ('register_date', models.DateTimeField(verbose_name=b'date registered')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=5)),
                ('quantity_assigned', models.IntegerField(default=1)),
                ('quantity_confirmed', models.IntegerField(default=1)),
                ('confirmed', models.BooleanField()),
                ('confirmation_date', models.DateTimeField(verbose_name=b'date confirmation')),
                ('enabled', models.BooleanField()),
                ('active', models.BooleanField()),
                ('register_date', models.DateTimeField(verbose_name=b'date registered')),
                ('event_id', models.ForeignKey(to='myEvent.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
