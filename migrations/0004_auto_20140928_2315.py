# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2014-09-28 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractApp', '0003_auto_20140928_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='quantity',
            field=models.IntegerField(null='FALSE'),
        ),
    ]