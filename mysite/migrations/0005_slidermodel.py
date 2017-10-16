# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('mysite', '0004_auto_20170709_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, to='cms.CMSPlugin', related_name='mysite_slidermodel', parent_link=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
