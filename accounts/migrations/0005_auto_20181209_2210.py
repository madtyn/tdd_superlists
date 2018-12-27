# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-09 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_token_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='token',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=40),
        ),
    ]
