# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyVehicle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('employee_no', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('block_number', models.CharField(max_length=5)),
                ('flat_number', models.CharField(max_length=5)),
                ('mobile_number', models.IntegerField()),
                ('user_photo', models.ImageField(upload_to='')),
                ('identity_card', models.FileField(upload_to='identity_card')),
                ('parking_slot_no', models.CharField(max_length=50)),
                ('vehicle_registration_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=32)),
                ('make_and_model', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('engine_number', models.CharField(max_length=100)),
                ('vehicle_insurance_no', models.CharField(max_length=100)),
                ('insurance_valid_upto', models.DateField()),
                ('vehicle_registration_card', models.FileField(upload_to='vehicle_registration_card')),
                ('vehicle_insurance', models.FileField(upload_to='vehicle_insurance')),
                ('vehicle_photo', models.ImageField(upload_to='')),
                ('driving_license_number', models.CharField(max_length=15)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license', models.FileField(upload_to='driving_license')),
                ('declaration', models.TextField(null=True, default='By submitting this form, I hereby declare that I will be obliged to the following terms and conditions:\n\n1) I will abide by the rules of Traffic,\n2) I will not cause inconvenience to other road users.', blank=True)),
                ('date_of_application', models.DateTimeField(null=True, blank=True)),
                ('registered_with_security_section', models.BooleanField()),
                ('vehicle_pass_no', models.CharField(null=True, blank=True, max_length=32)),
                ('registered_in_the_name_of', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('place_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='VehiclePass',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pass_number', models.IntegerField()),
                ('vehicle_no', models.CharField(max_length=20)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('vehicle_type', models.CharField(null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], blank=True, max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='parkingslot',
            old_name='parking_slot_name',
            new_name='parking_area_name',
        ),
        migrations.RemoveField(
            model_name='bustiming',
            name='route',
        ),
        migrations.RemoveField(
            model_name='bustiming',
            name='to_time',
        ),
        migrations.AddField(
            model_name='bustiming',
            name='availability',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bustiming',
            name='bus_no',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bustiming',
            name='ending_point',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bustiming',
            name='starting_point',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bustiming',
            name='working_day',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='residentlog',
            name='is_entering',
            field=models.BooleanField(verbose_name='Is the vehicle entering?'),
        ),
        migrations.AlterField(
            model_name='residentlog',
            name='vehicle_type',
            field=models.CharField(null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='declaration',
            field=models.TextField(null=True, default='By submitting this form, I hereby declare that I will be obliged to the following terms and conditions:\n\n1) I will abide by the rules of Traffic,\n2) I will not cause inconvenience to other road users.', blank=True),
        ),
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
            name='registered_with_security_section',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='user_photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='vehicle_insurance',
            field=models.FileField(upload_to='vehicle_insurance'),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='vehicle_photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='vehicle_registration_card',
            field=models.FileField(upload_to='vehicle_registration_card'),
        ),
        migrations.AlterField(
            model_name='suspiciousvehicle',
            name='vehicle_image',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='suspiciousvehicle',
            name='vehicle_type',
            field=models.CharField(null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='theftreport',
            name='status',
            field=models.CharField(default='not found', max_length=20),
        ),
        migrations.AlterField(
            model_name='theftreport',
            name='vehicle_type',
            field=models.CharField(null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='visitorlog',
            name='vehicle_type',
            field=models.CharField(null=True, choices=[('bicycle', 'bicycle'), ('bike', 'bike'), ('car', 'car'), ('truck', 'truck'), ('courier', 'courier'), ('auto', 'auto'), ('other', 'other')], blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='route',
            name='bus',
            field=models.ForeignKey(to='vms.BusTiming'),
        ),
        migrations.AddField(
            model_name='route',
            name='place',
            field=models.ForeignKey(to='vms.Place'),
        ),
        migrations.AddField(
            model_name='bustiming',
            name='bus_route',
            field=models.ManyToManyField(to='vms.Place', through='vms.Route'),
        ),
    ]
