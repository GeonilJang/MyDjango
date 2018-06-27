# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-27 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180628_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feeling',
            field=models.CharField(choices=[('g', 'Good'), ('b', 'Bad'), ('s', 'Sad')], default='g', max_length=1),
        ),
    ]
