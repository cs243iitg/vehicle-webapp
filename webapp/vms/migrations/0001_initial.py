# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentVehicle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_photo', models.ImageField(upload_to='')),
                ('vehicle_photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('roll_number', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('hostel_name', models.CharField(max_length=32)),
                ('room_number', models.CharField(max_length=5)),
                ('mobile_number', models.IntegerField()),
                ('driving_license_number', models.CharField(max_length=15)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('address_of_communication', models.TextField()),
                ('address_of_communication_district', models.CharField(max_length=100)),
                ('address_of_communication_state', models.CharField(max_length=100)),
                ('address_of_communication_pincode', models.IntegerField()),
                ('permanent_address', models.TextField()),
                ('permanent_address_district', models.CharField(max_length=100)),
                ('permanent_address_state', models.CharField(max_length=100)),
                ('permanent_address_pincode', models.IntegerField()),
                ('parents_emailid', models.EmailField(max_length=75)),
                ('parents_contact_no', models.IntegerField()),
                ('vehicle_registration_number', models.CharField(max_length=100)),
                ('registered_with_security_section', models.BooleanField()),
                ('color', models.CharField(max_length=32)),
                ('make_and_model', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('engine_number', models.CharField(max_length=100)),
                ('relation_with_owner', models.CharField(max_length=32)),
                ('vehicle_insurance_no', models.CharField(max_length=100)),
                ('insurance_valid_upto', models.DateField()),
                ('declaration', models.BooleanField()),
                ('date_of_application', models.DateTimeField()),
                ('identity_card', models.FileField(upload_to='')),
                ('driving_license', models.FileField(upload_to='')),
                ('vehicle_registration_card', models.FileField(upload_to='')),
                ('vehicle_insurance', models.FileField(upload_to='')),
                ('vehicle_pass_no', models.CharField(max_length=32)),
                ('registered_in_the_name_of', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
