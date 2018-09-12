# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, related_name='mysite_cardimage', primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('title_text', models.CharField(blank=True, max_length=50)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('image_url', models.CharField(blank=True, default='', max_length=100)),
                ('image_title', models.CharField(blank=True, default='', max_length=100)),
                ('color_class', models.CharField(default='grey lighten-5', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CardImageLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, related_name='mysite_cardimagelink', primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('title_text', models.CharField(blank=True, max_length=50)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('image_url', models.CharField(blank=True, default='', max_length=100)),
                ('image_title', models.CharField(blank=True, default='', max_length=100)),
                ('color_class', models.CharField(default='grey lighten-5', max_length=50)),
                ('link_text', models.CharField(blank=True, default='', max_length=100)),
                ('link_destination', models.CharField(blank=True, default='http://www.cosmostue.nl/', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CardLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, related_name='mysite_cardlink', primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('title_text', models.CharField(blank=True, max_length=50)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('color_class', models.CharField(default='grey lighten-5', max_length=50)),
                ('link_text', models.CharField(blank=True, default='', max_length=100)),
                ('link_destination', models.CharField(blank=True, default='http://www.cosmostue.nl/', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='card',
            name='image_title',
        ),
        migrations.RemoveField(
            model_name='card',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='card',
            name='link_destination',
        ),
        migrations.RemoveField(
            model_name='card',
            name='link_text',
        ),
    ]
