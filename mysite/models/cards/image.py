from cms.models.pluginmodel import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField


class CardImage(CMSPlugin):
    title_text = models.CharField(max_length=50, blank=True)
    content = HTMLField(blank=True)
    image_url = models.CharField(max_length=100, default='', blank=True)
    image_title = models.CharField(max_length=100, default='', blank=True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')
