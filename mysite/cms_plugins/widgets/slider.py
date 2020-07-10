from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mysite.models import SliderModel


class Slider(CMSPluginBase):
    """
    A slider plugin
    """
    render_template = './widgets/slider.html'  # The html this represents
    name = 'Slider (Width 12)'  # The name you will see in the browser editor
    module = 'Custom'  # A custom plugin that has specific functionality
    model = SliderModel  # The type in the database
    parent_classes = ['RowPlugin']  # What the plugin can be in


# Registers the plugin into the system
plugin_pool.register_plugin(Slider)
