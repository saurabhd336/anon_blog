# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('story', models.CharField(max_length=10000)),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2016, 6, 2, 22, 14, 14, 459000))),
            ],
        ),
    ]
