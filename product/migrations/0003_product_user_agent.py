# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-03 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180703_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_agent',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
