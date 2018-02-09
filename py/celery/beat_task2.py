# How to run a celery task:
# 1. make sure RabbitMQ is running in the background
# 2. $ celery -A tasks worker --loglevel=info

from celery import Celery
from celery.schedules import crontab

app = Celery('beat_task2', broker='pyamqp://guest@localhost//')
app.conf.beat_schedule = {
    'add-every-second': {
        'task': 'beat_task2.add',
        'schedule': 1.0,
        'args': (16, 15)
    },
}
app.conf.timezone = 'UTC'


@app.task
def add(x, y):
    print('{} + {} = {}'.format(x, y, x + y))
