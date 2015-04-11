# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0003_auto_20150411_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theftreport',
            name='reporter',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
