# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 4, 51, 47, 881000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 4, 51, 47, 881000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
