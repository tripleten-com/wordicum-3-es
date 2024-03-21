"""
Configuración WSGI para el proyecto wordicum.

Expone el WSGI que puede llamarse como una variable de nivel módulo llamada ``application``.

Para obtener más información acerca de este archivo, consulta
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordicum.settings')

application = get_wsgi_application()
