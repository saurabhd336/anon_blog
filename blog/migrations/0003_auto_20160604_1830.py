# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 18:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160604_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 4, 18, 30, 21, 527338)),
        ),
    ]
