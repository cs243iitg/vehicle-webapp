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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('bus_route', models.CharField(max_length=512)),
                ('from_time', models.TimeField()),
                ('bus_no', models.CharField(unique=True, max_length=10)),
                ('working_day', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('day', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeVehicle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('employee_no', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('block_number', models.CharField(max_length=5)),
                ('flat_number', models.CharField(max_length=5)),
                ('mobile_number', models.IntegerField()),
                ('user_photo', models.ImageField(upload_to='')),
                ('identity_card', models.FileField(null=True, upload_to='identity_card')),
                ('parking_slot_no', models.CharField(max_length=50)),
                ('vehicle_registration_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=32)),
                ('make_and_model', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('engine_number', models.CharField(max_length=100)),
                ('registered_in_the_name_of', models.CharField(max_length=100)),
                ('vehicle_insurance_no', models.CharField(unique=True, max_length=100)),
                ('insurance_valid_upto', models.DateField()),
                ('vehicle_registration_card', models.FileField(upload_to='vehicle_registration_card')),
                ('vehicle_insurance', models.FileField(null=True, upload_to='vehicle_insurance')),
                ('vehicle_photo', models.ImageField(null=True, upload_to='')),
                ('driving_license_number', models.CharField(max_length=15)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license', models.FileField(null=True, upload_to='driving_license')),
                ('declaration', models.TextField(null=True, blank=True, default='By submitting this form, I hereby declare that I will be obliged to the following terms and conditions:\n\n1) I will abide by the rules of Traffic,\n2) I will not cause inconvenience to other road users.')),
                ('date_of_application', models.DateTimeField(null=True, blank=True)),
                ('registered_with_security_section', models.BooleanField()),
                ('vehicle_pass_no', models.CharField(null=True, unique=True, blank=True, max_length=32)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('gate_name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('guard_phone_number', models.IntegerField()),
                ('is_security', models.BooleanField(help_text='Designates whether this user is security personnal or not.', default=False, verbose_name='Is security personnal')),
                ('guard_user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='guard_user')),
            ],
        ),
        migrations.CreateModel(
            name='IITGUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('is_student', models.BooleanField(help_text='Designates whether the user is a student or a professor.', default=False, verbose_name='Is student')),
                ('user', models.OneToOneField(default=False, to=settings.AUTH_USER_MODEL, related_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='OnDutyGuard',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('place', models.CharField(max_length=100)),
                ('is_gate', models.BooleanField()),
                ('guard', models.OneToOneField(to='vms.Guard', related_name='guard')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('parking_area_name', models.CharField(unique=True, max_length=100)),
                ('total_slots', models.IntegerField(null=True, blank=True, default=0)),
                ('available_slots', models.IntegerField(null=True, blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PersonPass',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('old_card_reference', models.CharField(max_length=10)),
                ('pass_number', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('user_photo', models.ImageField(upload_to='')),
                ('age', models.IntegerField()),
                ('identified_by', models.CharField(max_length=255)),
                ('work_area', models.CharField(max_length=255)),
                ('working_time', models.CharField(max_length=255)),
                ('nature_of_work', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('is_blocked', models.BooleanField()),
                ('reason_for_block', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('place_name', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentLog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('registration_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(null=True, blank=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], max_length=50)),
                ('vehicle_model', models.CharField(null=True, blank=True, max_length=100)),
                ('is_entering', models.BooleanField(verbose_name='Is the vehicle entering?')),
                ('gate', models.ForeignKey(null=True, to='vms.Gate')),
            ],
        ),
        migrations.CreateModel(
            name='StudentVehicle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('roll_number', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('hostel_name', models.CharField(max_length=32)),
                ('room_number', models.CharField(max_length=5)),
                ('mobile_number', models.IntegerField()),
                ('user_photo', models.ImageField(upload_to='')),
                ('identity_card', models.FileField(null=True, upload_to='identity_card')),
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
                ('vehicle_registration_number', models.CharField(unique=True, max_length=100)),
                ('color', models.CharField(max_length=32)),
                ('make_and_model', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('engine_number', models.CharField(max_length=100)),
                ('registered_in_the_name_of', models.CharField(max_length=100)),
                ('relation_with_owner', models.CharField(max_length=32)),
                ('vehicle_insurance_no', models.CharField(unique=True, max_length=100)),
                ('insurance_valid_upto', models.DateField()),
                ('vehicle_registration_card', models.FileField(null=True, upload_to='vehicle_registration_card')),
                ('vehicle_insurance', models.FileField(null=True, upload_to='vehicle_insurance')),
                ('vehicle_photo', models.ImageField(upload_to='')),
                ('driving_license_number', models.CharField(max_length=15)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license', models.FileField(null=True, upload_to='driving_license')),
                ('declaration', models.TextField(null=True, blank=True, default='By submitting this form, I hereby declare that I will be obliged to the following terms and conditions:\n\n1) I will abide by the rules of Traffic,\n2) I will not cause inconvenience to other road users.')),
                ('date_of_application', models.DateTimeField(null=True, blank=True)),
                ('registered_with_security_section', models.BooleanField()),
                ('vehicle_pass_no', models.CharField(null=True, unique=True, blank=True, max_length=32)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SuspiciousVehicle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('vehicle_number', models.CharField(unique=True, max_length=20)),
                ('vehicle_type', models.CharField(null=True, blank=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], max_length=50)),
                ('vehicle_model', models.CharField(null=True, blank=True, max_length=100)),
                ('vehicle_image', models.ImageField(null=True, blank=True, upload_to='suspicious_image')),
                ('remarks', models.TextField(null=True, blank=True, max_length=1000)),
                ('reporter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TheftReport',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('vehicle_pass_no', models.CharField(unique=True, max_length=50)),
                ('theft_time', models.DateTimeField(null=True)),
                ('theft_place', models.CharField(null=True, max_length=100)),
                ('remarks', models.TextField(null=True, blank=True, max_length=1000)),
                ('status', models.CharField(default='Submitted', choices=[('Submitted', 'Submitted'), ('Received by Security Section', 'Received by Security Section'), ('Search in Progress', 'Search in Progress'), ('Vehicle Found', 'Vehicle Found'), ('Case Closed (Vehicle Not Found)', 'Case Closed (Vehicle Not Found)'), ('Vehicle Returned', 'Vehicle Returned')], max_length=100)),
                ('emp_vehicle', models.ForeignKey(null=True, blank=True, to='vms.EmployeeVehicle')),
                ('reporter', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('stud_vehicle', models.ForeignKey(null=True, blank=True, to='vms.StudentVehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePass',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pass_number', models.CharField(unique=True, max_length=10)),
                ('vehicle_no', models.CharField(max_length=20)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('vehicle_type', models.CharField(null=True, blank=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(null=True, blank=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], max_length=50)),
                ('vehicle_model', models.CharField(null=True, blank=True, max_length=100)),
                ('driver_name', models.CharField(null=True, blank=True, max_length=255)),
                ('license_number', models.CharField(null=True, blank=True, max_length=20)),
                ('place_to_visit', models.CharField(null=True, blank=True, max_length=100)),
                ('purpose_of_visit', models.TextField(null=True, blank=True, max_length=1000)),
                ('in_time', models.DateTimeField(null=True, blank=True)),
                ('out_time', models.DateTimeField(null=True, blank=True)),
                ('in_gate', models.ForeignKey(null=True, to='vms.Gate', related_name='in_gate_log')),
                ('out_gate', models.ForeignKey(null=True, to='vms.Gate', related_name='out_gate_log')),
            ],
        ),
        migrations.AddField(
            model_name='bustiming',
            name='availability',
            field=models.ManyToManyField(to='vms.Day'),
        ),
        migrations.AddField(
            model_name='bustiming',
            name='ending_point',
            field=models.ForeignKey(to='vms.Place', related_name='ending_point'),
        ),
        migrations.AddField(
            model_name='bustiming',
            name='starting_point',
            field=models.ForeignKey(to='vms.Place', related_name='starting_point'),
        ),
    ]
