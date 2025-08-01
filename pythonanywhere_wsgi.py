# PythonAnywhere WSGI Configuration

import os
import sys

# Add your project directory to Python path
project_home = '/home/seuusername/readbook'  # Substitua pelo seu username
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
