# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0002_guard_guard_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeevehicle',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='suspiciousvehicle',
            name='reporter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
