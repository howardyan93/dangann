# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='client_mark',
            field=models.CharField(blank=True, default='web', max_length=10, null=True),
        ),
    ]
