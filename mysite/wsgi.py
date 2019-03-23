
import os
import sys

from django.core.wsgi import get_wsgi_application

path = '/home/cosmos/web/cosmoswebsite'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings_pr")

application = get_wsgi_application()
