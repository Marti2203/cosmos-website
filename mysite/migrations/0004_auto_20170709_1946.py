# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('mysite', '0003_facebookgallerymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookEventsModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', serialize=False, related_name='mysite_facebookeventsmodel', primary_key=True, auto_created=True, parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='facebookgallerymodel',
            name='color_class',
        ),
        migrations.RemoveField(
            model_name='facebookgallerymodel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='facebookgallerymodel',
            name='title_text',
        ),
    ]
