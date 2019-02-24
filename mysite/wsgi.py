
import os
import sys
import site

from django.core.wsgi import get_wsgi_application

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/cosmos/web/cosmoswebsite/env_cosmosweb_36/lib/python3.6/site-packages')

# Add the app's directory to the PYTHONPATH
path = '/home/cosmos/web/cosmoswebsite'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings_pr")

# Activate virtual env
activate_env=os.path.expanduser("/home/cosmos/web/cosmoswebsite/env_cosmosweb_36/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()
