from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# set the default django settings module for the celery program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insboot.settings")

app = Celery("insboot")

app.config_from_object("django.conf:settings")
app.conf.broker_url = "redis://localhost"
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
