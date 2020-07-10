from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mysite.models import ColumnPlugin


class Column4Plugin(CMSPluginBase):
    """
    Column that is a third of the row it is in.
    """

    render_template = './structure/column4.html'  # The html this represents
    # The name you will see in the browser editor
    name = 'Column (Width 4)'
    model = ColumnPlugin  # The type in the database
    # What exactly plugin it is. A Structure plugin defines only the format of the website
    module = 'Structure'

    child_classes = ['Card', 'CardImage', 'CardLink',
                     'CardImageLink']  # What can be contained inside of the plugin
    allow_children = True  # Whether this component can have children

    parent_classes = ['RowPlugin']  # The parent in which a column can be.
    require_parent = True  # A column is always inside a row.


# Registers the plugin into the system
plugin_pool.register_plugin(Column4Plugin)
