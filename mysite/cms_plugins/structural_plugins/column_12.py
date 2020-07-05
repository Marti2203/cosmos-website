from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mysite.models import ColumnPlugin


class Column12Plugin(CMSPluginBase):
    """
    Column that takes the full size of the row it is in.
    """

    render_template = './structure/column12.html'  # The html this represents
    # The name you will see in the browser editor
    name = 'Column (Width 12)'
    model = ColumnPlugin  # The type in the database
    # What exactly plugin it is. A Structure plugin defines only the format of the website
    module = 'Structure'

    # What can be contained inside of the plugin
    child_classes = ['Card', 'CardImage',
                     'CardLink', 'CardImageLink', 'Slider']
    allow_children = True  # Whether this component can have children

    parent_classes = ['RowPlugin']  # The parent in which a column can be.
    require_parent = True  # A column is always inside a row.


# Registers the plugin into the system
plugin_pool.register_plugin(Column12Plugin)
