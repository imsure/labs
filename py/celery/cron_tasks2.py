# How to run a celery task:
# 1. make sure RabbitMQ is running in the background
# 2. $ celery -A tasks worker --loglevel=info

from celery import Celery
from celery.schedules import crontab

from datetime import datetime
import pytz

app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.conf.beat_schedule = {
    # Executes every 15-minute
    'execute-every-15-minute': {
        'task': 'cron_tasks.task_every_15_minutes',
        'schedule': crontab(minute='*/15'),
        'args': (16, 16),
    },
}
app.conf.timezone = 'UTC'
# app.conf.timezone = 'US/Pacific'


@app.task
def task_every_15_minutes():
    utc_now = datetime.now()
