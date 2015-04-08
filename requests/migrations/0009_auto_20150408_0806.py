# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requests', '0008_auto_20150407_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestAccept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='available',
            name='id',
        ),
        migrations.AlterField(
            model_name='available',
            name='username',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 13, 6, 0, 334000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 13, 6, 0, 334000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='requestaccept',
            name='request_id',
            field=models.ForeignKey(to='requests.Request'),
        ),
        migrations.AddField(
            model_name='requestaccept',
            name='username',
            field=models.ForeignKey(related_name='ra_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
