# How to run a celery task:
# 1. make sure RabbitMQ is running in the background
# 2. $ celery -A tasks worker --loglevel=info

from celery import Celery
from celery.schedules import crontab

from datetime import datetime
import pytz

app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.conf.beat_schedule = {
    'task-every-minute': {
        'task': 'cron_tasks.print_time',
        'schedule': crontab(minute='*/1'),
        # 'schedule': crontab(hour=20, minute=1, day_of_week=5),
        # 'schedule': crontab(hour=20, minute=42, day_of_week=5),
    },
    'task-every-5-minute': {
        'task': 'cron_tasks.print_time_5',
        'schedule': crontab(minute='*/5'),
    },
}
app.conf.timezone = 'UTC'
# app.conf.enable_utc = False
# app.conf.timezone = 'US/Pacific'


day_of_week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


@app.task
def print_time():
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    now_utc = datetime.now(pytz.timezone('UTC'))
    now_pst = now_utc.astimezone(pytz.timezone('US/Pacific'))
    print('Task scheduled every minute at UTC time {} - {}'.format(day_of_week[now_utc.weekday()], now_utc.strftime(fmt)))
    print('\tPST time {} - {}'.format(day_of_week[now_pst.weekday()], now_pst.strftime(fmt)))


@app.task
def print_time_5():
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    now_utc = datetime.now(pytz.timezone('UTC'))
    now_pst = now_utc.astimezone(pytz.timezone('US/Pacific'))
    print('Task scheduled every 5 minutes at UTC time {} - {}'.format(day_of_week[now_utc.weekday()], now_utc.strftime(fmt)))
    print('\tPST time {} - {}'.format(day_of_week[now_pst.weekday()], now_pst.strftime(fmt)))


@app.task
def multiply(x, y):
    print('{} * {} = {}'.format(x, y, x * y))
