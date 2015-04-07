# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'John', max_length=30)),
                ('category_name', models.CharField(default=b'A Category', max_length=100)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 4, 7, 4, 14, 37, 166000, tzinfo=utc))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_by', models.CharField(default=b'John', max_length=30)),
                ('name', models.CharField(default=b'A Project', max_length=100)),
                ('time_in_hours', models.DecimalField(max_digits=4, decimal_places=2)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 4, 7, 4, 14, 37, 170000, tzinfo=utc))),
                ('number_of_people', models.DecimalField(max_digits=2, decimal_places=0)),
                ('category_name', models.ForeignKey(to='requests.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
