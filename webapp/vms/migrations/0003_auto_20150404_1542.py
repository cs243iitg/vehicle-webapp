# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vms', '0002_auto_20150403_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('route', models.CharField(max_length=255)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gate_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('guard_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('parking_slot_name', models.CharField(max_length=100)),
                ('total_slots', models.IntegerField(default=0, null=True, blank=True)),
                ('available_slots', models.IntegerField(default=0, null=True, blank=True)),
                ('security_on_duty', models.ForeignKey(to='vms.Guard', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('registration_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50, null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], blank=True)),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('is_entering', models.BooleanField(verbose_name='Is the vehicle entering?')),
                ('gate', models.ForeignKey(to='vms.Gate', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuspiciousVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(max_length=50, null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], blank=True)),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('vehicle_image', models.ImageField(upload_to='', null=True, blank=True)),
                ('remarks', models.TextField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TheftReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('reporter_name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50, null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True)),
                ('theft_time', models.DateTimeField(null=True, blank=True)),
                ('theft_place', models.CharField(max_length=100, null=True, blank=True)),
                ('remarks', models.TextField(max_length=1000, null=True, blank=True)),
                ('reporter', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(max_length=50, null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], blank=True)),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('driver_name', models.CharField(max_length=255, null=True, blank=True)),
                ('license_number', models.CharField(max_length=20, null=True, blank=True)),
                ('place_to_visit', models.CharField(max_length=100, null=True, blank=True)),
                ('purpose_of_visit', models.TextField(max_length=1000, null=True, blank=True)),
                ('in_time', models.DateTimeField(null=True, blank=True)),
                ('out_time', models.DateTimeField(null=True, blank=True)),
                ('in_gate', models.ForeignKey(to='vms.Gate', null=True, related_name='in_gate_log')),
                ('out_gate', models.ForeignKey(to='vms.Gate', null=True, related_name='out_gate_log')),
            ],
        ),
        migrations.AddField(
            model_name='gate',
            name='security_on_duty',
            field=models.ForeignKey(to='vms.Guard', null=True, blank=True),
        ),
    ]
