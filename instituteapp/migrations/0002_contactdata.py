# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-24 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emai', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('courses', multiselectfield.db.fields.MultiSelectField(choices=[('py', 'Python'), ('dj', 'Django'), ('ui', 'UI'), ('rest', 'Rest API')], max_length=200)),
                ('shift', multiselectfield.db.fields.MultiSelectField(choices=[('mrg', 'Morning'), ('aftn', 'Afternoon'), ('eveng', 'Evening'), ('night', 'Night')], max_length=200)),
                ('location', multiselectfield.db.fields.MultiSelectField(choices=[('hyd', 'Hyderabad'), ('bang', 'Banglore'), ('che', 'Chennai'), ('pune', 'Pune')], max_length=200)),
                ('gender', models.CharField(max_length=50)),
                ('start_date', models.DateField(max_length=100)),
            ],
        ),
    ]
