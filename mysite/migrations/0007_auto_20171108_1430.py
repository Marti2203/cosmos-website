# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='program',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
    ]
