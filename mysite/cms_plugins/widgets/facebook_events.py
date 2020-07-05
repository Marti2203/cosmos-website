from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mysite.models import ParentPlugin, ColumnPlugin, Card, CardImageLink, CardImage, CardLink, FacebookGalleryModel, FacebookEventsModel, SliderModel
from mysite.services.facebook import FacebookService


class FacebookEvents(CMSPluginBase):
    """
    A plugin to display the events which are defined in the facebook page for cosmos
    """
    render_template = './widgets/events.html'  # The html this represents
    # The name you will see in the browser editor
    name = 'Facebook Events (Width 12)'
    module = 'Custom'  # A module with user defined behaviour
    model = FacebookEventsModel  # The type in the database

    parent_classes = ['RowPlugin']  # Where the plugin can be put

    def render(self, context, instance, placeholder):
        instance.future_events = FacebookService.get_future_events()
        instance.past_events = FacebookService.get_past_events()
        context = super(FacebookEvents, self).render(
            context, instance, placeholder)
        return context


# Registers the plugin into the system
plugin_pool.register_plugin(FacebookEvents)
