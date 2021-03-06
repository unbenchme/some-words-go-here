# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0007_auto_20150407_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available',
            name='username',
            field=models.OneToOneField(related_name='a_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 3, 38, 18, 779000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 3, 38, 18, 779000, tzinfo=utc)),
        ),
    ]
