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
            name='BusTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('route', models.CharField(max_length=255)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gate_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guard_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parking_slot_name', models.CharField(max_length=100)),
                ('total_slots', models.IntegerField(default=0, null=True, blank=True)),
                ('available_slots', models.IntegerField(default=0, null=True, blank=True)),
                ('security_on_duty', models.ForeignKey(blank=True, to='vms.Guard', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(blank=True, max_length=50, null=True, choices=[(b'bicycle', b'bicycle'), (b'bike', b'bike'), (b'car', b'car'), (b'truck', b'truck'), (b'courier', b'courier'), (b'auto', b'auto'), (b'other', b'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('is_entering', models.BooleanField(verbose_name=b'Is the vehicle entering?')),
                ('gate', models.ForeignKey(to='vms.Gate', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('roll_number', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('hostel_name', models.CharField(max_length=32)),
                ('room_number', models.CharField(max_length=5)),
                ('mobile_number', models.IntegerField()),
                ('user_photo', models.ImageField(upload_to=b'')),
                ('identity_card', models.FileField(upload_to=b'identity_card')),
                ('address_of_communication', models.TextField()),
                ('address_of_communication_district', models.CharField(max_length=100)),
                ('address_of_communication_state', models.CharField(max_length=100)),
                ('address_of_communication_pincode', models.IntegerField()),
                ('permanent_address', models.TextField()),
                ('permanent_address_district', models.CharField(max_length=100)),
                ('permanent_address_state', models.CharField(max_length=100)),
                ('permanent_address_pincode', models.IntegerField()),
                ('parents_contact_no', models.IntegerField()),
                ('parents_emailid', models.EmailField(max_length=75)),
                ('vehicle_registration_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=32)),
                ('make_and_model', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('engine_number', models.CharField(max_length=100)),
                ('relation_with_owner', models.CharField(max_length=32)),
                ('vehicle_insurance_no', models.CharField(max_length=100)),
                ('insurance_valid_upto', models.DateField()),
                ('vehicle_registration_card', models.FileField(upload_to=b'vehicle_registration_card')),
                ('vehicle_insurance', models.FileField(upload_to=b'vehicle_insurance')),
                ('vehicle_photo', models.ImageField(upload_to=b'')),
                ('driving_license_number', models.CharField(max_length=15)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license', models.FileField(upload_to=b'driving_license')),
                ('declaration', models.TextField(default=b'By submitting this form, I hereby declare that I will be obliged to the following terms and conditions:\n\n1) I will abide by the rules of Traffic,\n2) I will not cause inconvenience to other road users.', null=True, blank=True)),
                ('date_of_application', models.DateTimeField(null=True, blank=True)),
                ('registered_with_security_section', models.BooleanField(default=False)),
                ('vehicle_pass_no', models.CharField(max_length=32, null=True, blank=True)),
                ('registered_in_the_name_of', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SuspiciousVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(blank=True, max_length=50, null=True, choices=[(b'bicycle', b'bicycle'), (b'bike', b'bike'), (b'car', b'car'), (b'truck', b'truck'), (b'courier', b'courier'), (b'auto', b'auto'), (b'other', b'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('vehicle_image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('remarks', models.TextField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TheftReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reporter_name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50, null=True, choices=[(b'bicycle', b'bicycle'), (b'bike', b'bike'), (b'car', b'car'), (b'truck', b'truck'), (b'courier', b'courier'), (b'auto', b'auto'), (b'other', b'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True)),
                ('theft_time', models.DateTimeField(null=True, blank=True)),
                ('theft_place', models.CharField(max_length=100, null=True, blank=True)),
                ('remarks', models.TextField(max_length=1000, null=True, blank=True)),
                ('status', models.CharField(default=b'not found', max_length=20)),
                ('reporter', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(blank=True, max_length=50, null=True, choices=[(b'bicycle', b'bicycle'), (b'bike', b'bike'), (b'car', b'car'), (b'truck', b'truck'), (b'courier', b'courier'), (b'auto', b'auto'), (b'other', b'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('driver_name', models.CharField(max_length=255, null=True, blank=True)),
                ('license_number', models.CharField(max_length=20, null=True, blank=True)),
                ('place_to_visit', models.CharField(max_length=100, null=True, blank=True)),
                ('purpose_of_visit', models.TextField(max_length=1000, null=True, blank=True)),
                ('in_time', models.DateTimeField(null=True, blank=True)),
                ('out_time', models.DateTimeField(null=True, blank=True)),
                ('in_gate', models.ForeignKey(related_name='in_gate_log', to='vms.Gate', null=True)),
                ('out_gate', models.ForeignKey(related_name='out_gate_log', to='vms.Gate', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='gate',
            name='security_on_duty',
            field=models.ForeignKey(blank=True, to='vms.Guard', null=True),
        ),
    ]
