"""
WSGI config for excel_parser project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_parser.settings')
application = get_wsgi_application()

project_folder = os.path.expanduser('~/excel_parser')
load_dotenv(os.path.join(project_folder, '.env'))
