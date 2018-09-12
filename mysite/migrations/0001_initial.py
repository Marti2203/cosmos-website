# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='mysite_card', parent_link=True, to='cms.CMSPlugin')),
                ('title_text', models.CharField(max_length=50, blank=True)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('image_url', models.CharField(max_length=100, blank=True, default='')),
                ('image_title', models.CharField(max_length=100, blank=True, default='')),
                ('color_class', models.CharField(max_length=50, default='grey lighten-5')),
                ('link_text', models.CharField(max_length=100, blank=True, default='')),
                ('link_destination', models.CharField(max_length=100, blank=True, default='http://www.cosmostue.nl/')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ColumnPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='mysite_columnplugin', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ParentPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='mysite_parentplugin', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
