# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_token_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.CharField(default='', max_length=255),
        ),
    ]
