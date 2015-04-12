# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bustiming',
            name='bus_no',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='employeevehicle',
            name='vehicle_pass_no',
            field=models.CharField(blank=True, null=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='personpass',
            name='pass_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='vehicle_pass_no',
            field=models.CharField(blank=True, null=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='suspiciousvehicle',
            name='vehicle_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='theftreport',
            name='registration_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
