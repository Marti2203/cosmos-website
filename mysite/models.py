from cms.models.pluginmodel import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField

############################
# Models for Content Cards #
############################
class CardImageLink(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    image_url = models.CharField(max_length=100, default='', blank = True)
    image_title = models.CharField(max_length=100, default='', blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')
    link_text = models.CharField(max_length=100, default='', blank = True)
    link_destination = models.CharField(max_length=100, default='http://www.cosmostue.nl/', blank = True)

class CardImage(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    image_url = models.CharField(max_length=100, default='', blank = True)
    image_title = models.CharField(max_length=100, default='', blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')

class CardLink(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')
    link_text = models.CharField(max_length=100, default='', blank = True)
    link_destination = models.CharField(max_length=100, default='http://www.cosmostue.nl/', blank = True)

class Card(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')

#########################
#   Structural Models 	#
#########################
class ColumnPlugin(CMSPlugin):
    name = 'column'

class ParentPlugin(CMSPlugin):
	name = "Parent"        

#########################
#     Widget Models 	#
#########################
class SliderModel(CMSPlugin):
    name = 'Slider Model'

class FacebookGalleryModel(CMSPlugin):
    name = 'Cosmos facebook gallery model'

class FacebookEventsModel(CMSPlugin):
    name = 'Cosmos facebook events model'
    
