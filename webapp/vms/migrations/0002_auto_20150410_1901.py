# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='bus',
        ),
        migrations.RemoveField(
            model_name='route',
            name='place',
        ),
        migrations.RemoveField(
            model_name='bustiming',
            name='bus_route',
        ),
        migrations.AddField(
            model_name='bustiming',
            name='bus_route',
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
