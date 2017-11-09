from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import ParentPlugin, ColumnPlugin, Card, CardImageLink, CardImage, CardLink, FacebookGalleryModel, FacebookEventsModel, SliderModel
import requests

##########################################
# Structural Plugins (Rows, Columns)     #
##########################################
class RowPlugin(CMSPluginBase):
    render_template = '/structure/row.html'
    name = 'Row (Width 12)'
    model = ParentPlugin
    module = 'Structure'
    child_classes=['Column4Plugin', 'Column6Plugin', 'Column8Plugin', 'Column12Plugin', 'FacebookGallery','FacebookEvents']
    allow_children = True
    def render(self, context, instance, placeholder):
        context = super(RowPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(RowPlugin)


class Column4Plugin(CMSPluginBase):
    render_template = '/structure/column4.html'
    name = 'Column (Width 4)'
    model = ColumnPlugin
    parent_classes=['RowPlugin']
    child_classes=['Card', 'CardImage', 'CardLink', 'CardImageLink']
    module = 'Structure'
    allow_children = True
    require_parent = True  # Is it required that this plugin is a child of another plugin?
    # You can also specify a list of plugins that are accepted as parents,
    # or leave it away completely to accept all
    # parent_classes = ['ParentCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super(Column4Plugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(Column4Plugin)

class Column6Plugin(CMSPluginBase):
    render_template = '/structure/column6.html'
    name = 'Column (Width 6)'
    model = ColumnPlugin
    child_classes=['Card', 'CardImage', 'CardLink', 'CardImageLink']
    parent_classes=['RowPlugin']
    module = 'Structure'
    allow_children = True
    require_parent = True  # Is it required that this plugin is a child of another plugin?
    # You can also specify a list of plugins that are accepted as parents,
    # or leave it away completely to accept all
    # parent_classes = ['ParentCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super(Column6Plugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(Column6Plugin)

class Column12Plugin(CMSPluginBase):
    render_template = '/structure/column12.html'
    name = 'Column (Width 12)'
    parent_classes=['RowPlugin']
    child_classes=['Card', 'CardImage', 'CardLink', 'CardImageLink', 'Slider']
    model = ColumnPlugin
    allow_children = True
    module = 'Structure'
    require_parent = True  # Is it required that this plugin is a child of another plugin?
    # You can also specify a list of plugins that are accepted as parents,
    # or leave it away completely to accept all
    # parent_classes = ['ParentCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super(Column12Plugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(Column12Plugin)

class Column8Plugin(CMSPluginBase):
    render_template = '/structure/column8.html'
    name = 'Column (Width 8)'
    module = 'Structure'
    child_classes=['Card', 'CardImage', 'CardLink', 'CardImageLink']
    parent_classes=['RowPlugin']
    model = ColumnPlugin
    allow_children = True
    require_parent = True  # Is it required that this plugin is a child of another plugin?
    # You can also specify a list of plugins that are accepted as parents,
    # or leave it away completely to accept all
    # parent_classes = ['ParentCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super(Column8Plugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(Column8Plugin)

##########################################
# Card Plugins (Content)			     #
##########################################
class CardImageLink(CMSPluginBase):
    render_template = '/cards/card-image-link.html'
    name = 'Card (Image + Link)'
    model = CardImageLink
    parent_classes=['Column4Plugin', 'Column6Plugin', 'Column8Plugin', 'Column12Plugin']
    module = 'Structure'
    allow_children = True
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(CardImageLink, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CardImageLink)

class CardImage(CMSPluginBase):
    render_template = '/cards/card-image.html'
    name = 'Card (Image)'
    model = CardImage
    parent_classes=['Column4Plugin', 'Column6Plugin', 'Column8Plugin', 'Column12Plugin']
    module = 'Structure'
    allow_children = True
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(CardImage, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CardImage)

class CardLink(CMSPluginBase):
    render_template = '/cards/card-link.html'
    name = 'Card (Link)'
    model = CardLink
    parent_classes=['Column4Plugin', 'Column6Plugin', 'Column8Plugin', 'Column12Plugin']
    module = 'Structure'
    allow_children = True
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(CardLink, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(CardLink)

class Card(CMSPluginBase):
    render_template = '/cards/card.html'
    name = 'Card (Basic)'
    model = Card
    parent_classes=['Column4Plugin', 'Column6Plugin', 'Column8Plugin', 'Column12Plugin']
    module = 'Structure'
    allow_children = True
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(Card, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(Card)



###################################################
# Wisget Plugins (Facebook Gallery, Slider etc.)  #
###################################################
class FacebookGallery(CMSPluginBase):
	model = FacebookGalleryModel
	render_template = '/widgets/gallery.html'
	name = 'Facebook Gallery (Width 12)'
	parent_classes=['RowPlugin']
	module = 'Custom'

	def render(self, context, instance, placeholder):
		if "=" in context['request'].get_full_path():
			album_id = context['request'].get_full_path().split('=')[1]
			r = requests.get('https://graph.facebook.com/v2.9/'+album_id+'/?fields=photos.limit(1000){images},description,name&access_token=521350984877058|ucRdnLYj2pZpMmcfZQAaw-RcARg')
		else:	
			r = requests.get('https://graph.facebook.com/v2.9/372136979547549/?fields=albums.limit(500){cover_photo{images},name,photo_count}&access_token=521350984877058|ucRdnLYj2pZpMmcfZQAaw-RcARg')
		instance.variable = r.json()
		context = super(FacebookGallery, self).render(context, instance, placeholder)
		return context

plugin_pool.register_plugin(FacebookGallery)

class Slider(CMSPluginBase):
	model = SliderModel
	render_template = '/widgets/slider.html'
	name = 'Slider (Width 12)'
	parent_classes=['RowPlugin']
	module = 'Custom'
	def render(self, context, instance, placeholder):
		context = super(Slider, self).render(context, instance, placeholder)
		return context

plugin_pool.register_plugin(Slider)

class FacebookEvents(CMSPluginBase):
	model = FacebookEventsModel
	render_template = '/widgets/events.html'
	name = 'Facebook Events (Width 12)'
	parent_classes=['RowPlugin']
	module = 'Custom'
	def render(self, context, instance, placeholder):
		r =  requests.get('https://graph.facebook.com/v2.9/372136979547549/?fields=events.limit(40){cover,name,start_time,description}&access_token=521350984877058|ucRdnLYj2pZpMmcfZQAaw-RcARg')
		instance.variable = r.json()
		context = super(FacebookEvents, self).render(context, instance, placeholder)
		return context

plugin_pool.register_plugin(FacebookEvents)
