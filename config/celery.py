import os
from celery import Celery

# Point to our Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Load settings from Django's settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in all apps
app.autodiscover_tasks()
