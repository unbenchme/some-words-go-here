# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 5, 4, 37, 470000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='username',
            field=models.ForeignKey(related_name='c_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='created_by',
            field=models.ForeignKey(related_name='r_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 5, 4, 37, 470000, tzinfo=utc)),
        ),
    ]
