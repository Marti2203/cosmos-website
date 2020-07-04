from cms.models.pluginmodel import CMSPlugin
from .door import Door
from .pi import Pi
from .profile import Profile
from .token import Token
from .cards import *
from .widgets import *


#########################
#   Structural Models 	#
#########################
class ColumnPlugin(CMSPlugin):
    name = 'column'


class ParentPlugin(CMSPlugin):
    name = "Parent"


__all__ = ['ColumnPlugin', 'ParentPlugin', 'Door', 'Pi', 'Profile', 'Token', 'cards', 'widgets']
