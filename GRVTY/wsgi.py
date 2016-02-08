"""
WSGI config for GRVTY project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'GRVTY.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
