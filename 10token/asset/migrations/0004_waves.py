# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-19 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20170919_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
            ],
        ),
    ]
