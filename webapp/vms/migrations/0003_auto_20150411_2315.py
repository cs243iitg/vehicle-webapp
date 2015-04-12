# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0002_auto_20150411_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guard',
            name='guard_name',
        ),
        migrations.RemoveField(
            model_name='guard',
            name='id',
        ),
        migrations.AddField(
            model_name='guard',
            name='iitguser_ptr',
            field=models.OneToOneField(parent_link=True, serialize=False, auto_created=True, default=1, primary_key=True, to='vms.IITGUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='iitguser',
            name='user',
            field=models.OneToOneField(related_name='user', default=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
