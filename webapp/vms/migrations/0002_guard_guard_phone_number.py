# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guard',
            name='guard_phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
