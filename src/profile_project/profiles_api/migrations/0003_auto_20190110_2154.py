# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='created_on',
            new_name='create_on',
        ),
    ]
