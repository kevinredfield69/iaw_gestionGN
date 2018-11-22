"""
WSGI config for gestion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os,sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion.settings")

sys.path.append('/home/debian/iaw_gestionGN')

#sys.path.insert(0, '/var/www/html/iaw_gestionGN')
activate_this = '/home/debian/env/django/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

application = get_wsgi_application()
