# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20171108_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='card_number',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='key_access',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='member_type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_nr',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='tue_id',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
