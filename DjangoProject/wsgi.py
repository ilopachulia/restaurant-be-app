import os
import sys
from django.core.wsgi import get_wsgi_application

path = '/home/iliapachulia/restaurant-be-app/DjangoProject/settings.py'
if path not in sys.path:
    sys.path.insert(0, path)



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings")

application = get_wsgi_application()
