# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard_apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='user_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]