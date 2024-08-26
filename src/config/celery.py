import os
from celery.schedules import crontab

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_connection_retry_on_startup = True  # This is to ensure that the worker retries to connect to the broker on startup.

app.conf.beat_schedule = {
    "user_update_status": {
        "task": "core.tasks.update_active_user_status_to_present",
        "schedule": crontab(hour=12, minute=46),
    },
}
