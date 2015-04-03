# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentvehicle',
            name='driving_license',
            field=models.FileField(upload_to='driving_license'),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='identity_card',
            field=models.FileField(upload_to='identity_card'),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='vehicle_insurance',
            field=models.FileField(upload_to='vehicle_insurance'),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='vehicle_registration_card',
            field=models.FileField(upload_to='vehicle_registration_card'),
        ),
    ]
