# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_auto_20171124_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='employee',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
