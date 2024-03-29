import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJPR.settings')

app = Celery('DJPR')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'weekly_notification': {
        'task': 'news.tasks.weekly_notification',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday')
    },
}

app.autodiscover_tasks()
