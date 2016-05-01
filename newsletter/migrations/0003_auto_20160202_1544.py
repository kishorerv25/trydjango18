# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 2, 10, 14, 13, 739538, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 2, 10, 14, 34, 337349, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
