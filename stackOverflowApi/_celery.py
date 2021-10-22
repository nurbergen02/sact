import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackOverflowApi.settings.py')

app = Celery('stackOverflowApi')
app.config_from_object('django.conf:settings.py', namespace='CELERY')
app.autodiscover_tasks()


