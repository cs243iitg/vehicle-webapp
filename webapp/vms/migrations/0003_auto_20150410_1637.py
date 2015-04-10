# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0002_auto_20150410_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bustiming',
            name='availability',
            field=models.CharField(default=None, max_length=3, choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')]),
        ),
        migrations.AlterField(
            model_name='bustiming',
            name='bus_route',
            field=models.ManyToManyField(related_name='bus_route', to='vms.Place', through='vms.Route'),
        ),
        migrations.AlterField(
            model_name='bustiming',
            name='ending_point',
            field=models.ForeignKey(related_name='ending_point', to='vms.Place'),
        ),
        migrations.AlterField(
            model_name='bustiming',
            name='starting_point',
            field=models.ForeignKey(related_name='starting_point', to='vms.Place'),
        ),
    ]
