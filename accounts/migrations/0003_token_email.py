# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
