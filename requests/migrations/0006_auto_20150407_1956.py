# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_auto_20150407_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'John', max_length=30)),
                ('is_available', models.BooleanField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 0, 56, 55, 230000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 0, 56, 55, 230000, tzinfo=utc)),
        ),
    ]
