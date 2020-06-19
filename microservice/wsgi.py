"""
WSGI config for microservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microservice.settings')

application = get_wsgi_application()

microservice = os.path.expanduser('~/Team-Granite')
load_dotenv(os.path.join(microservice, '.env'))
