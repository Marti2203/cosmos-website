from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mysite.models import ParentPlugin


class RowPlugin(CMSPluginBase):
    """ 
    A page is made out of plugins which are displayed. This is the main plugin, could be called a page.
    """
    render_template = './structure/row.html'  # The html this represents
    # The name you will see in the browser editor
    name = 'Row (Width 12)'
    model = ParentPlugin  # The type in the database
    # What exactly plugin it is. A Structure plugin defines only the format of the website
    module = 'Structure'

    child_classes = ['Column4Plugin', 'Column6Plugin', 'Column8Plugin',
                     'Column12Plugin', 'FacebookGallery', 'FacebookEvents']  # What can be contained inside of the plugin

    allow_children = True  # Whether it can have children


plugin_pool.register_plugin(RowPlugin)  # Registers the plugin into the system
