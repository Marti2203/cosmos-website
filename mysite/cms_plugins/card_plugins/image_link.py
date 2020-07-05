from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mysite.models import CardImageLink


class CardImageLink(CMSPluginBase):
    """
    An object that contains both an image with a link to open with text besides it.
    """
    render_template = './cards/card-image-link.html'  # The html this represents

    # The name you will see in the browser editor
    name = 'Card (Image + Link)'
    model = CardImageLink  # The type in the database
    # What exactly plugin it is. A Structure plugin defines only the format of the website
    module = 'Structure'

    # What the plugin can be in
    parent_classes = ['Column4Plugin', 'Column6Plugin',
                      'Column8Plugin', 'Column12Plugin']
    # Whether this component can have children. This plugin can contain anything as a child
    allow_children = True
    require_parent = True  # A Card is in a column


# Registers the plugin into the system
plugin_pool.register_plugin(CardImageLink)
