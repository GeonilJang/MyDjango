# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-28 16:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prfile',
            new_name='Profile',
        ),
    ]
