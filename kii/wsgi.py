import os

from django.core.wsgi import get_wsgi_application

from kii.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kii.settings')

application = get_wsgi_application()

