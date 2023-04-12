"""
WSGI config for realestate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

# Adjust the Python path to include your Django project's directory
sys.path.append('/path/to/your/django/project')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'realestate.settings'

# Start the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
