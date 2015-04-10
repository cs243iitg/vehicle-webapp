# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('vms', '0002_auto_20150410_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='IITGUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('is_student', models.BooleanField(default=False, verbose_name='student_or_professor', help_text='Designates whether the user is a student or a professor.')),
                ('is_security', models.BooleanField(default=False, verbose_name='security_personnal', help_text='Designates whether this user is security personnal or not.')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonPass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('old_card_reference', models.CharField(max_length=10)),
                ('pass_number', models.CharField(max_length=10)),
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
            ],
        ),
        migrations.AlterField(
            model_name='facultyvehicle',
            name='registered_in_the_name_of',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentvehicle',
            name='registered_in_the_name_of',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='suspiciousvehicle',
            name='reporter',
            field=models.ForeignKey(to='vms.IITGUser'),
        ),
        migrations.AlterField(
            model_name='theftreport',
            name='reporter',
            field=models.ForeignKey(null=True, to='vms.IITGUser', blank=True),
        ),
        migrations.AddField(
            model_name='facultyvehicle',
            name='user',
            field=models.ForeignKey(default=1, to='vms.IITGUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentvehicle',
            name='user',
            field=models.ForeignKey(default=1, to='vms.IITGUser'),
            preserve_default=False,
        ),
    ]
