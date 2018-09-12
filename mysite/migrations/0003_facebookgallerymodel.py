# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('mysite', '0002_auto_20170702_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookGalleryModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='mysite_facebookgallerymodel', serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin')),
                ('title_text', models.CharField(max_length=50, blank=True)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('color_class', models.CharField(max_length=50, default='grey lighten-5')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
