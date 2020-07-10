from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from mysite.models import CardImage


class CardImage(CMSPluginBase):
    """
    An object that contains an image with text besides it.
    """
    render_template = './cards/card-image.html'  # The html this represents
    name = 'Card (Image)'  # The name you will see in the browser editor
    model = CardImage  # The type in the database
    # What exactly plugin it is. A Structure plugin defines only the format of the website
    module = 'Structure'

    # What the plugin can be in
    parent_classes = ['Column4Plugin', 'Column6Plugin',
                      'Column8Plugin', 'Column12Plugin']

    # Whether this component can have children. This plugin can contain anything as a child
    allow_children = True
    require_parent = True  # A Card is in a column


# Registers the plugin into the system
plugin_pool.register_plugin(CardImage)
