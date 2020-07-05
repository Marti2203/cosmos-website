from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from mysite.models import ParentPlugin, ColumnPlugin, Card, CardImageLink, CardImage, CardLink, FacebookGalleryModel, FacebookEventsModel, SliderModel
from mysite.services.facebook import  FacebookService

class FacebookGallery(CMSPluginBase):
    """ 
    Displays all facebook albums. Display of each album is done in custom view with template gallery_album
    """
    render_template = './widgets/gallery.html'  # The html this represents
    # The name you will see in the browser editor
    name = 'Facebook Gallery (Width 12)'
    module = 'Custom'  # This is a custom plugin. It has user defined functionality
    model = FacebookGalleryModel  # The type in the database
    parent_classes = ['RowPlugin']  # What the plugin can be in

    #Before rendering the template, we get some data from the facebook API service
    def render(self, context, instance, placeholder):
        # TODO RENAME THIS "VARIABLE"
        instance.variable = FacebookService.get_albums()
        instance.context_m = context
        context = super(FacebookGallery, self).render(
            context, instance, placeholder)
        return context


# Registers the plugin into the system
plugin_pool.register_plugin(FacebookGallery)
