# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 05:53
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('loginandreg', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
