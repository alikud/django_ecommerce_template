from __future__ import absolute_import

import os

from celery import Celery
from core.settings import INSTALLED_APPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('parser_app', backend="redis", broker='redis://localhost')
app.autodiscover_tasks(lambda: INSTALLED_APPS)
