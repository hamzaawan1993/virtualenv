# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_auto_20171124_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='employee_id',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
